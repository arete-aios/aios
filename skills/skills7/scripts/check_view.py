#!/usr/bin/env python3
"""SKILLS7: check a skill viewer without a browser.

  python3 -B check_view.py <skill-dir> [--public-dir DIR]

Checks: index.html is current; SKILL.md and manifest versions agree; relative Markdown links in
embedded files resolve inside the skill (links to files left out of the ZIP are listed as notes);
the page's own JavaScript ZIP equals the Python ZIP byte for byte; an optional public export
exists, matches its receipt and contains no owner data. Browser layout is not checked here.
"""
import argparse, base64, json, re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_view import render, sha, store_zip, private_markers  # noqa: E402


def slug(text):
    return re.sub(r'\s+', '-', re.sub(r'[^\w\s-]', '', text.lower(), flags=re.U).strip())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('skill'); ap.add_argument('--public-dir')
    a = ap.parse_args()
    skill = Path(a.skill).resolve()
    errors, notes, checks = [], [], {}
    m, data, page, _ = render(skill, False)
    index = skill / 'index.html'
    checks['indexUpToDate'] = index.exists() and index.read_bytes() == page
    if not checks['indexUpToDate']:
        errors.append('index.html is not the current build; run build_view.py')
    head = (skill / 'SKILL.md').read_text() if (skill / 'SKILL.md').exists() else ''
    hit = re.search(r'^\s*version:\s*"?([\w.\-]+)"?', head, re.M)
    checks['versionsAgree'] = bool(hit) and hit.group(1) == m['version']
    if not checks['versionsAgree']:
        errors.append(f"SKILL.md version {hit.group(1) if hit else None} != manifest {m['version']}")
    files, linked = data['files'], 0
    for rel, f in files.items():
        if not rel.endswith('.md') or rel.startswith('history/'):
            continue
        for target in re.findall(r'\[[^\]]+\]\(<?([^)\s>]+)>?\)', f['text']):
            parts = urlsplit(target)
            if parts.scheme or target.startswith(('#', '//', 'mailto:')):
                continue
            dest = (skill / rel).parent / unquote(parts.path)
            try:
                resolved = dest.resolve(); inside = resolved.is_relative_to(skill)
            except OSError:
                inside = False
            if not inside:
                notes.append(f'{rel} links outside the skill: {target}'); continue
            if not resolved.exists():
                errors.append(f'missing link {rel} -> {target}'); continue
            linked += 1
            key = str(resolved.relative_to(skill))
            if parts.fragment and key.endswith('.md'):
                heads = {slug(h) for h in re.findall(r'^#{1,6}\s+(.+)$', resolved.read_text(), re.M)}
                if unquote(parts.fragment) not in heads:
                    errors.append(f'missing anchor {rel} -> {target}')
            if f['zip'] and resolved.is_file() and not (key in files and files[key]['zip']):
                notes.append(f'{rel} links to {key}, which is not in the ZIP')
    checks['markdownLinksChecked'] = linked
    js = subprocess.run(['node', str(HERE / 'verify_zip.js'), str(index)], capture_output=True, text=True)
    py = store_zip(data['zip']['root'], data['zip']['order'], files)
    checks['zipJsEqualsPython'] = js.returncode == 0 and base64.b64decode(js.stdout) == py
    if not checks['zipJsEqualsPython']:
        errors.append('page ZIP differs from Python ZIP: ' + js.stderr.strip())
    checks['zip'] = {'files': len(data['zip']['order']), 'bytes': len(py), 'sha256': sha(py)}
    if a.public_dir:
        out = Path(a.public_dir); stem = f"{m['id']}-{m['version']}"
        receipt = json.loads((out / f'{stem}.json').read_text())
        html, zipped = (out / f'{stem}.html').read_bytes(), (out / f'{stem}.zip').read_bytes()
        _, public_data, public_page, _ = render(skill, True)
        public_zip = store_zip(public_data['zip']['root'], public_data['zip']['order'], public_data['files'])
        public_js = subprocess.run(['node', str(HERE / 'verify_zip.js'), str(out / f'{stem}.html')], capture_output=True, text=True)
        leaks = [n for n in private_markers(m) if n.encode() in html or n.encode() in zipped]
        checks['public'] = {'htmlMatchesReceipt': sha(html) == receipt['html']['sha256'], 'zipMatchesReceipt': sha(zipped) == receipt['zip']['sha256'],
                            'htmlMatchesCurrentBuild': html == public_page,
                            'zipEqualsPublicBuild': zipped == public_zip,
                            'publicJsEqualsPython': public_js.returncode == 0 and base64.b64decode(public_js.stdout) == public_zip,
                            'ownerDataLeaks': len(leaks)}
        if leaks or not all(v for k, v in checks['public'].items() if k != 'ownerDataLeaks'):
            errors.append(f"public export problem: {checks['public']}")
    print(json.dumps({'skill': m['id'], 'version': m['version'], 'ok': not errors, 'checks': checks, 'errors': errors, 'notes': notes}, ensure_ascii=False, indent=1))
    sys.exit(0 if not errors else 1)


if __name__ == '__main__':
    main()
