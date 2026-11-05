# Structural report contract

Parent: [DASHBOARD7](../SKILL.md). Schema `aios-map/1`, release 1.1.0.

The scanner emits only this allowlisted object. The webpage rejects unknown fields,
unexpected types and invalid ranges. It never renders file text, names or paths.

```json
{
  "schema": "aios-map/1",
  "origin": "local-metadata",
  "scope_complete": true,
  "files_seen": 12,
  "limits_hit": false,
  "layers": {
    "constitution": {"state": "found", "files": 1},
    "memory": {"state": "found", "files": 6},
    "skills": {"state": "found", "files": 3},
    "tools": {"state": "not_found", "files": 0},
    "focus": {"state": "found", "files": 2}
  }
}
```

States are `found`, `not_found`, or `unknown`. Counts are integers 0–5000.
`found` means a recognised root-level layer file or directory contained at least
one visible regular file within scope. A directory alone is insufficient. A bounded
or unreadable search sets completeness false; absent layers then remain unknown.
Recognition is intentionally conservative. Custom structures require owner review.

No date, owner identifier, filename, directory name, source text, hash, free-text
field, URL, integration name or credential is accepted. A structural report can still
reveal aspects of an organisation's setup; the owner must decide whether to share it.
The scanner does not upload anything. The demo imports it into memory in the current
tab; it does not store it in localStorage, send it to Arete or create a Network post.
