#!/usr/bin/env python3
"""Read-only structural inventory of an Arete skill. No network, mutation or quality score.

Usage: audit_package.py <skill-dir> [--workspace-root <root>]
JSON on stdout; exit 1 for structural errors, 0 otherwise. Missing optional
manifest/view is reported as an observation for a method-only skill.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path


def inspect(skill, workspace=None):
    skill = Path(skill).resolve()
    workspace = Path(workspace).resolve() if workspace else None
    report = {'schema': 1, 'kind': 'structural-audit', 'writes': False,
              'errors': [], 'observations': [], 'files': [], 'dependencies': [],
              'manual_review': ['trigger and result', 'decision rules and realistic behavior',
                                'AIOS contribution and standalone use', 'permission boundaries',
                                'privacy of all exported text', 'actual tool availability']}
    errors, observations = report['errors'], report['observations']
    if workspace and not skill.is_relative_to(workspace):
        errors.append('Skill directory escapes workspace')
        return report
    if not skill.is_dir():
        errors.append('Skill directory is missing')
        return report
    manifest, view = {}, {}
    for name, destination in [('manifest.json', manifest), ('view.json', view)]:
        path = skill / name
        if path.is_symlink() and not path.resolve().is_relative_to(skill):
            errors.append(f'{name}: path escapes package')
        elif path.exists():
            try:
                value = json.loads(path.read_text(encoding='utf-8'))
                if not isinstance(value, dict):
                    raise ValueError('object required')
                destination.update(value)
            except (ValueError, OSError) as exc:
                errors.append(f'{name}: invalid or unreadable JSON ({type(exc).__name__})')
        else:
            observations.append(f'{name}: absent; human viewer not inventoried')
    source = skill / 'SKILL.md'
    if not source.is_file() or not source.resolve().is_relative_to(skill):
        errors.append('SKILL.md is missing or escapes package')
    else:
        try:
            text = source.read_text(encoding='utf-8')
            front = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
            if not front:
                errors.append('SKILL.md: frontmatter missing')
            else:
                for field in ('name', 'description'):
                    value = re.search(r'^' + field + r':\s*(\S.*)$', front[1], re.M)
                    if not value or value[1].strip() in ('""', "''", '|', '>'):
                        # Block descriptions can be valid; leave YAML semantics to its validator.
                        if value and value[1].strip() in ('|', '>'):
                            observations.append(f'{field}: YAML block; validate with skill frontmatter validator')
                        else:
                            errors.append(f'SKILL.md: {field} missing or empty')
                version = re.search(r'^  version:\s*[\"\']?([^\"\'\s]+)', front[1], re.M)
                if version and manifest.get('version') and version[1] != manifest['version']:
                    errors.append('SKILL.md and manifest version differ')
        except (UnicodeError, OSError):
            errors.append('SKILL.md: unreadable UTF-8')
    declared = manifest.get('resources', [])
    if not isinstance(declared, list) or not all(isinstance(x, str) for x in declared):
        errors.append('manifest resources must be a string list')
        declared = []
    if len(declared) != len(set(declared)):
        errors.append('Duplicate manifest resource')
    for name in ('id', 'name', 'version'):
        if manifest and not isinstance(manifest.get(name), str):
            errors.append(f'manifest {name} missing or not a string')
    group_files = []
    try:
        group_files = [f['path'] for g in view.get('fileGroups', []) for f in g['files']]
        if not all(isinstance(x, str) for x in group_files):
            raise TypeError()
    except (KeyError, TypeError):
        errors.append('Invalid view fileGroups')
        group_files = []
    for rel in sorted(set(declared + group_files + ['SKILL.md'] +
                          [n for n in ('manifest.json', 'view.json') if (skill / n).exists()])):
        path = (skill / rel).resolve()
        if Path(rel).is_absolute() or not path.is_relative_to(skill):
            errors.append(f'{rel}: path escapes package')
            continue
        if not path.is_file():
            errors.append(f'{rel}: file missing')
            continue
        digest = hashlib.sha256()
        try:
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(65536), b''):
                    digest.update(block)
            report['files'].append({'path': rel, 'bytes': path.stat().st_size,
                                    'sha256': digest.hexdigest()})
        except OSError:
            errors.append(f'{rel}: file unreadable')
    dependencies = manifest.get('dependencies', [])
    if not isinstance(dependencies, list):
        errors.append('manifest dependencies must be a list')
        dependencies = []
    for dep in dependencies:
        if not isinstance(dep, dict):
            errors.append('Invalid dependency entry')
            continue
        item = {'id': dep.get('id'), 'status': 'declared-only'}
        if 'path' in dep and (not isinstance(dep['path'], str) or not dep['path'].strip()):
            errors.append(f"Dependency {dep.get('id')}: path must be a nonempty string")
            item['status'] = 'invalid-path'
        elif dep.get('path') and workspace:
            target = (workspace / dep['path']).resolve()
            if not target.is_relative_to(workspace):
                errors.append(f"Dependency {dep.get('id')}: escapes workspace")
                item['status'] = 'outside-workspace'
            else:
                item['status'] = 'present' if target.exists() else 'missing'
                if not target.exists():
                    observations.append(f"Dependency {dep.get('id')}: not present here")
        report['dependencies'].append(item)
    report['skill_id'] = manifest.get('id')
    report['version'] = manifest.get('version')
    report['ok'] = not errors
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill_dir')
    parser.add_argument('--workspace-root')
    args = parser.parse_args()
    result = inspect(args.skill_dir, args.workspace_root)
    result['ok'] = not result['errors']
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
