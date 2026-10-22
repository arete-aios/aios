#!/usr/bin/env python3
"""SKILLS7: build a skill's human viewer (index.html) from its manifest.json and view.json.

  python3 -B build_view.py <skill-dir>                 write <skill-dir>/index.html (internal view)
  python3 -B build_view.py <skill-dir> --check         exit 1 if index.html is not up to date
  python3 -B build_view.py <skill-dir> --public <dir>  write shareable <id>-<version>.html/.zip/.json without owner data

Fonts, logo, page template and required provider icons are bundled in this portable SKILLS7 engine.
No network and no timestamps: the same inputs give the same bytes.
"""
import argparse, base64, hashlib, json, re, struct, sys, zlib
from pathlib import Path
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
SKILLS7 = HERE.parent
ASSETS = SKILLS7 / 'assets'
LIBRARY = ASSETS / 'icons'
NEUTRAL = {'ai', 'chat', 'file', 'doc', 'link', 'mail', 'play', 'sliders', 'collect', 'send', 'loop', 'check', 'eye', 'user', 'build', 'shield', 'skill'}
PRIVATE = {'OWNER_ONLY', 'OWNER_BUSINESS', 'PRIVATE'}
DOS_DATE = ((2026 - 1980) << 9) | (10 << 5) | 20
sha = lambda b: hashlib.sha256(b).hexdigest()


def private_markers(manifest):
    """Owner identifiers and specific receipt links must never reach a public export."""
    owner = manifest.get('owner_setup') or {}
    return [x for x in [owner.get('summary')] + [l.get('file') for l in owner.get('links', [])]
            + [a.get('identifier') for a in owner.get('accounts', [])] if x]


def en(x):
    return x if isinstance(x, str) else (x or {}).get('en', '')


def inside(base: Path, rel: str) -> Path:
    path = (base / rel).resolve()
    if not path.is_relative_to(base.resolve()):
        raise SystemExit(f'path escapes the skill folder: {rel}')
    return path


def read_text(base: Path, rel: str):
    data = inside(base, rel).read_bytes()
    text = data.decode('utf-8')
    assert text.encode('utf-8') == data, f'{rel} does not round-trip as UTF-8'
    return data, text


def file_record(data: bytes, zipped: bool):
    """Keep text inspectable and binary assets byte-exact in the in-page archive."""
    try:
        text = data.decode('utf-8')
        if '\0' in text:
            raise UnicodeError('binary content')
        return {'bytes': len(data), 'text': text, 'encoding': 'utf-8', 'zip': zipped}
    except UnicodeError:
        return {'bytes': len(data), 'base64': base64.b64encode(data).decode('ascii'),
                'encoding': 'base64', 'zip': zipped}


def record_bytes(record: dict) -> bytes:
    return base64.b64decode(record['base64'], validate=True) if record.get('encoding') == 'base64' else record['text'].encode('utf-8')


def store_zip(root: str, order: list, files: dict) -> bytes:
    """Same bytes as makeZip() in the page: store method, fixed date, UTF-8 names."""
    parts, central, offset = [], [], 0
    for rel in order:
        name, data = f'{root}/{rel}'.encode(), record_bytes(files[rel])
        crc = zlib.crc32(data) & 0xFFFFFFFF
        parts += [struct.pack('<IHHHHHIIIHH', 0x04034B50, 20, 0x0800, 0, 0, DOS_DATE, crc, len(data), len(data), len(name), 0), name, data]
        central += [struct.pack('<IHHHHHHIIIHHHHHII', 0x02014B50, 20, 20, 0x0800, 0, 0, DOS_DATE, crc, len(data), len(data), len(name), 0, 0, 0, 0, 0, offset), name]
        offset += 30 + len(name) + len(data)
    cd = b''.join(central)
    return b''.join(parts) + cd + struct.pack('<IHHHHIIH', 0x06054B50, 0, 0, len(order), len(order), len(cd), offset, 0)


def dig(obj, dotted: str):
    for key in dotted.split('.'):
        obj = obj[key]
    return obj


def license_of(skill: Path, m: dict) -> str:
    raw = ''
    if (skill / 'SOURCE.json').exists():
        raw = json.loads((skill / 'SOURCE.json').read_text()).get('license', '')
    if not raw and (skill / 'SKILL.md').exists():
        hit = re.search(r'^license:\s*(\S+)', (skill / 'SKILL.md').read_text(), re.M)
        raw = hit.group(1) if hit else ''
    return {'CC-BY-4.0': 'CC BY 4.0'}.get(raw, raw)


def assemble(skill: Path, public: bool):
    m = json.loads((skill / 'manifest.json').read_text(encoding='utf-8'))
    public = public or m.get('distribution') == 'community'
    v = json.loads((skill / 'view.json').read_text(encoding='utf-8'))
    gen = json.loads((SKILLS7 / 'manifest.json').read_text(encoding='utf-8'))['version']
    used = {'manifest.json': sha((skill / 'manifest.json').read_bytes()), 'view.json': sha((skill / 'view.json').read_bytes())}

    files, order = {}, []
    for group in v['fileGroups']:
        for f in group['files']:
            data = inside(skill, f['path']).read_bytes()
            if public and f['path'] == 'manifest.json':
                exported = dict(m)
                exported.pop('owner_setup', None)
                if 'runs' in exported:
                    exported['runs'] = [r for r in exported['runs']
                                        if str(r.get('audience', '')).upper() not in PRIVATE]
                text = json.dumps(exported, ensure_ascii=False, indent=2) + '\n'
                data = text.encode('utf-8')
            files[f['path']] = file_record(data, bool(group.get('zip')))
            used[f['path']] = sha(data)
            if group.get('zip'):
                order.append(f['path'])

    # A complete source archive may also contain binary fonts/images and the
    # local engine. Exclude generated HTML to avoid recursive self-embedding.
    if m.get('archive', {}).get('files') is not None:
        order = m['archive']['files']
        assert len(order) == len(set(order)), 'duplicate archive file'
        assert 'index.html' not in order, 'generated index.html cannot include itself'
        for rel in order:
            if rel not in files:
                blob = inside(skill, rel).read_bytes()
                files[rel] = file_record(blob, True)
                used[rel] = sha(blob)
            files[rel]['zip'] = True
        for rel in files:
            if rel not in order:
                files[rel]['zip'] = False

    hidden = set(v.get('hiddenTools', []))
    icons_override = v.get('toolIcons', {})
    tools = {t['id']: {'name': t['name'], 'icon': icons_override.get(t['id'], t.get('icon_id')), 'importance': t.get('importance'),
                       'requirement': t.get('requirement'), 'purpose': t.get('purpose'), 'scope': t.get('scope'), 'limit': t.get('limit')}
             for t in m.get('tools', [])}
    groups = [{'id': g['id'], 'title': g['title'], 'description': g.get('description'), 'requirement_label': g.get('requirement_label'),
               'tools': [t for t in g['tools'] if t not in hidden], 'steps': v.get('groupSteps', {}).get(g['id'], [])}
              for g in m.get('tool_groups', [])]
    workflow = {w['number']: {k: w.get(k) for k in ('name', 'label', 'output', 'doc')} for w in m.get('workflow', [])}

    o = m.get('overview', {})
    overview = {'eyebrow': v.get('eyebrow') or {'en': f"{m['name']} · {en(m['title'])}", 'lv': f"{m['name']} · {m['title'].get('lv', en(m['title'])) if isinstance(m['title'], dict) else m['title']}"},
                'title': o.get('title') or m['title'], 'summary': o.get('summary') or m.get('purpose'),
                'prompt': o.get('starting_prompt'), 'onboarding': v.get('onboarding'),
                'additionalPrompts': o.get('additional_prompts', [])}

    advanced = v.get('advanced')
    if advanced:
        data = json.loads(read_text(skill, advanced['data'])[1])
        used[advanced['data']] = sha(inside(skill, advanced['data']).read_bytes())
        advanced = dict(advanced, vars={k: dig(data, p) for k, p in advanced.get('vars', {}).items()},
                        bars=[dict(b, value=dig(data, b['value'])) for b in advanced.get('bars', [])])
        advanced.pop('data')

    runs = [{k: r.get(k) for k in ('title', 'status', 'summary', 'date', 'version', 'output', 'url', 'urlLabel')} for r in m.get('runs', [])
            if not (public and str(r.get('audience', '')).upper() in PRIVATE)]
    owner = None
    if not public and m.get('owner_setup'):
        s = m['owner_setup']
        for account in s.get('accounts', []):
            if account.get('url'):
                u = urlsplit(account['url'])
                assert u.scheme == 'https' and u.hostname and not u.username and not u.password, 'account link must be an HTTPS page without credentials'
        owner = {'status': s.get('status'), 'summary': s.get('summary'), 'links': [{'title': l['title'], 'href': l['file']} for l in s.get('links', [])]}
        for field in ('accounts', 'locations', 'currentFiles', 'archives', 'cadence', 'helper', 'extensions', 'connections', 'socialMode', 'browser'):
            if field in s:
                owner[field] = s[field]

    # Every document a button can open must be embedded.
    wanted = [w['doc'].split('#')[0] for w in workflow.values() if w.get('doc')]
    wanted += [p for n in (v.get('flow') or {}).get('nodes', []) for p in n.get('files', [])]
    wanted += [x for x in (overview['onboarding'], v.get('scoreDoc')) if x] + [r['output'] for r in runs if r.get('output')]
    wanted += [p['file'] for p in overview['additionalPrompts'] if p.get('file')]
    if v.get('preview', {}).get('sourceDoc'):
        wanted.append(v['preview']['sourceDoc'])
    wanted += [d['file'] for guide in v.get('guides', {}).values()
               for section in guide.get('sections', []) for d in section.get('docs', [])]
    wanted += [d['file'] for d in v.get('layout', {}).get('behavior', {}).get('docs', [])]
    if v.get('layout', {}).get('settings', {}).get('storageDoc'):
        wanted.append(v['layout']['settings']['storageDoc'])
    for field in ('helperFile', 'connectionsDoc'):
        if v.get('layout', {}).get('settings', {}).get(field):
            wanted.append(v['layout']['settings'][field])
    for rel in wanted:
        assert rel in files, f'linked document is not listed in view.json fileGroups: {rel}'
    flow = v.get('flow')
    if flow:
        ids = {n['id'] for n in flow['nodes']}
        for a, b, *_ in flow['edges']:
            assert a in ids and b in ids, (a, b)
        for n in flow['nodes']:
            assert not n.get('tool') or n['tool'] in tools, n['id']

    need = {t['icon'] for t in tools.values() if t['icon']} | {n['icon'] for n in (flow or {}).get('nodes', [])} | {r.get('icon', 'skill') for r in v.get('related', [])}
    need.update(a['icon'] for a in (owner or {}).get('accounts', []))
    need.update(a['icon'] for a in v.get('layout', {}).get('sourceSummary', {}).get('pending', []))
    if flow and flow.get('presentation') == 'journey':
        sequence = flow['sequence']
        assert len(sequence) == len(set(sequence)) and all(x in ids for x in sequence), 'invalid journey sequence'
        assert [next(n['step'] for n in flow['nodes'] if n['id'] == x) for x in sequence] == list(range(1, len(sequence) + 1)), 'journey steps must be consecutive'
        assert flow.get('start') in ids, 'invalid journey start'
        if flow.get('modeBehavior') == 'canvas':
            simple = flow['simple']
            simple_ids = {n['id'] for n in simple['nodes']}
            assert flow.get('defaultMode') in {'simple', 'detailed'}, 'invalid default canvas mode'
            for n in simple['nodes']:
                assert n['target'] in sequence, 'simple node target is not a detail step'
                assert 0 <= n['x'] <= simple['width'] - 110 and 0 <= n['y'] <= simple['height'] - 110, 'simple node outside canvas'
                need.add(n['icon'])
            assert all(a in simple_ids and b in simple_ids for a, b, *_ in simple['edges']), 'invalid simple edge'
        for n in flow['nodes']:
            assert not n.get('detailFor') or n['detailFor'] in sequence, 'artifact detail target is not a step'
            need.update(c['icon'] for c in n.get('channels', []))
            if n.get('companion'):
                need.add(n['companion'])
            need.update(n.get('headerIcons', []))
        channels = flow.get('channels') or {}
        need.update(c['icon'] for c in channels.get('current', []) + channels.get('optional', []))
    icons = {}
    for name in sorted(need - NEUTRAL):
        for src in (skill / 'assets/tool-logos' / f'{name}.svg', LIBRARY / f'{name}.svg'):
            if src.exists():
                icons[name] = re.sub(r'<title>.*?</title>', '', src.read_text().strip()); used['engine/assets/icons/' + name + '.svg'] = sha(src.read_bytes()); break
        else:
            raise SystemExit(f'icon not bundled in this skill or the local SKILLS7 engine: {name}')

    ui = json.loads((ASSETS / 'ui.json').read_text(encoding='utf-8'))
    if v.get('layout'):
        ui['tab_example'] = {'en': 'Example', 'lv': 'Piemērs'}
        ui['tab_settings'] = {'en': 'My setup', 'lv': 'Mani iestatījumi'}
        if 'principles' in v['layout']['tabs']:
            ui['tab_principles'] = {'en': 'Principles', 'lv': 'Principi'}
        if 'aios' in v['layout']['tabs']:
            ui['tab_aios'] = {'en': 'AIOS', 'lv': 'AIOS'}
        if v['layout'].get('changesOnly'):
            ui['tab_log'] = {'en': 'Changes', 'lv': 'Izmaiņas'}
    ui.update(v.get('ui', {}))
    zip_size = len(store_zip(m['id'], order, files))
    owner_label = m.get('owner', {}).get('label') if isinstance(m.get('owner'), dict) else m.get('owner')
    data = {
        'skill': {'id': m['id'], 'name': m['name'], 'version': m['version'], 'updated_on': m.get('updated_on'), 'author': m.get('author'),
                  'owner': owner_label, 'status': m.get('status_label'), 'resources': len(m.get('resources', [])) or None, 'license': license_of(skill, m)},
        'defaultLang': (m.get('ui') or {}).get('default_language', 'en'),
        'github': {k: m['github'].get(k) for k in ('url', 'public_version')} if m.get('github') else None,
        'overview': overview, 'example': v.get('example'),
        'related': [dict(r, links=[l for l in r.get('links', []) if not (public and l.get('internal'))]) for r in v.get('related', [])],
        'scorecard': m.get('scorecard'), 'scoreHint': v.get('scoreHint'), 'scoreDoc': v.get('scoreDoc'), 'rating': m.get('tool_rating'),
        'tools': tools, 'groups': groups, 'workflow': workflow, 'how': v.get('how'), 'filesLead': v.get('filesLead'),
        'fileTypes': v.get('fileTypes', []), 'fileGroups': v['fileGroups'], 'files': files,
        'zip': {'root': m['id'], 'order': order, 'count': len(order), 'bytes': zip_size, 'kb': round(zip_size / 1024)},
        'advanced': advanced, 'flow': flow, 'outputPreviews': m.get('output_previews'), 'runs': runs,
        'changelog': m.get('changelog', []), 'owner': owner, 'internal': not public,
        'compare': None if public else v.get('compare'), 'ui': ui,
        'icons': icons, 'build': {'generator': gen, 'mode': 'public' if public else 'internal', 'manifestSha': used['manifest.json']},
    }
    if v.get('layout'):
        assert set(v['layout']['tabs']) <= {'overview', 'how', 'flow', 'example', 'settings', 'log', 'principles', 'aios'}, 'unknown layout tab'
        if v['layout'].get('overview', {}).get('compact'):
            assert {'overview', 'flow', 'example'} <= set(v['layout']['tabs']), 'compact overview needs flow and example tabs'
        if v['layout'].get('filesTab'):
            assert v['layout']['filesTab'] in v['layout']['tabs'] and v['layout']['filesTab'] in v.get('guides', {}), 'file library needs a guide tab'
        for pending in v['layout'].get('sourceSummary', {}).get('pending', []):
            assert isinstance(pending['match'], str) and pending['match'].strip(), 'pending source needs a nonempty match'
        settings_tabs = v['layout'].get('settings', {}).get('tabs')
        if settings_tabs:
            assert v['layout']['settings'].get('compact') and set(settings_tabs) == {'setup', 'changes'}, 'settings tabs require compact setup/changes'
        anchors = [s['id'] for g in v.get('guides', {}).values() for s in g.get('sections', []) if s.get('id')]
        assert len(anchors) == len(set(anchors)) and all(re.fullmatch(r'guide-[a-z0-9-]+', x) for x in anchors), 'invalid guide anchors'
        for alias, route in v['layout'].get('routes', {}).items():
            assert re.fullmatch(r'[a-z][a-z0-9-]*', alias) and alias not in v['layout']['tabs'], 'invalid legacy route'
            assert route['tab'] in v['layout']['tabs'], 'legacy route target missing'
            if route.get('settingsView'):
                assert route['tab'] == 'settings' and settings_tabs and route['settingsView'] in settings_tabs, 'invalid settings route'
            if route.get('anchor'):
                assert any(s.get('id') == route['anchor'] for s in v.get('guides', {}).get(route['tab'], {}).get('sections', [])), 'legacy route anchor missing'
        data['layout'] = json.loads(json.dumps(v['layout']))
        if public and settings_tabs:
            # Keep method history accessible without exporting a private setup page.
            data['layout']['tabs'] = ['log' if x == 'settings' else x for x in data['layout']['tabs']]
            data['layout']['routes'] = {k: r for k, r in data['layout'].get('routes', {}).items() if r['tab'] != 'settings'}
        if v.get('guides'):
            data['guides'] = v['guides']
        if v.get('preview'):
            data['preview'] = v['preview']
    return m, data, used


def render(skill: Path, public: bool):
    m, data, used = assemble(skill, public)
    fonts = (ASSETS / 'fonts/fonts.css').read_text()
    fonts = re.sub(r"url\('([^']+\.woff2)'\)", lambda x: "url('data:font/woff2;base64," + base64.b64encode((ASSETS / 'fonts' / x.group(1)).read_bytes()).decode() + "')", fonts)
    logo = re.sub(r'\s(width|height)="\d+"', '', (ASSETS / 'logo-areteaios.svg').read_text().strip(), count=2)
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    title = f"{m['name']} — {en(m['title'])}"
    page = (ASSETS / 'viewer.html').read_text(encoding='utf-8')
    # Opt-in code is absent from legacy pages; no mass rebuild or unrelated byte changes.
    if not data['flow'] or data['flow'].get('presentation') != 'journey':
        page = re.sub(r'/\*JOURNEY:start\*/.*?/\*JOURNEY:end\*/\n?', '', page, flags=re.S)
    if not data.get('layout'):
        page = re.sub(r'/\*LAYOUT:start\*/.*?/\*LAYOUT:end\*/\n?', '', page, flags=re.S)
    page = page.replace('@@TITLE@@', title.replace('&', '&amp;').replace('<', '&lt;')).replace('@@FONTS@@', fonts).replace('@@LOGO@@', logo).replace('@@DATA@@', payload)
    shell = page.replace(payload, '')
    assert '@@' not in shell, 'unreplaced placeholder'
    assert not re.search(r'<script[^>]+src=|<link[^>]+href=|@import|url\((?![\'"]?(?:data:|#))', shell), 'external resource in page shell'
    if public:
        for needle in private_markers(m):
            assert not needle or needle not in page, f'private owner data in public export: {needle[:40]}'
    return m, data, page.encode('utf-8'), used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('skill'); ap.add_argument('--check', action='store_true'); ap.add_argument('--public', metavar='DIR')
    a = ap.parse_args()
    skill = Path(a.skill).resolve()
    if a.public:
        m, data, page, used = render(skill, True)
        out = Path(a.public).resolve(); out.mkdir(parents=True, exist_ok=True)
        stem = f"{m['id']}-{m['version']}"
        zipped = store_zip(m['id'], data['zip']['order'], data['files'])
        (out / f'{stem}.html').write_bytes(page); (out / f'{stem}.zip').write_bytes(zipped)
        receipt = {'skill': m['id'], 'version': m['version'], 'generator': data['build']['generator'], 'html': {'bytes': len(page), 'sha256': sha(page)},
                   'zip': {'files': len(data['zip']['order']), 'bytes': len(zipped), 'sha256': sha(zipped)}, 'ownerDataIncluded': False}
        (out / f'{stem}.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
        print(json.dumps(receipt, ensure_ascii=False)); return
    m, data, page, used = render(skill, False)
    target = skill / 'index.html'
    if a.check:
        ok = target.exists() and target.read_bytes() == page
        print(json.dumps({'skill': m['id'], 'indexUpToDate': ok, 'sha256': sha(page)}))
        sys.exit(0 if ok else 1)
    target.write_bytes(page)
    print(json.dumps({'skill': m['id'], 'version': m['version'], 'index': {'bytes': len(page), 'sha256': sha(page)},
                      'zipFiles': data['zip']['count'], 'zipBytes': data['zip']['bytes'], 'sourcesRead': used}, ensure_ascii=False))


if __name__ == '__main__':
    main()
