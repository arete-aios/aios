#!/usr/bin/env python3
"""Read-only, no-content structural inventory. Parent: ../SKILL.md.

Output contains fixed states and bounded counts only. No network or filesystem writes.
"""
import argparse
import json
import os
import stat
from pathlib import Path

LAYERS = ("constitution", "memory", "skills", "tools", "focus")
SKIP = frozenset({"secrets", "secret", "auth", "credentials", "node_modules", "vendor",
                  "cache", "caches", "backups", "archive", "archives", "system",
                  "runtime", "dist", "build", "__pycache__"})
ROOT_FILES = {"constitution.md", "business-constitution.md", "agents.md", "claude.md"}
MAX_FILES = 5000


def layer_for(name):
    folded = name.casefold().replace("_", "-")
    for layer in LAYERS:
        if folded == layer or folded in {f"0{n}-{layer}" for n in range(1, 7)}:
            return layer
    return None


def scan(root, max_entries=5000, max_depth=6):
    root = Path(root)
    if root.is_symlink() or not root.is_dir() or root.name.casefold() in SKIP:
        raise ValueError("Choose a real, readable working folder, not a link or excluded store.")
    result = {"schema": "aios-map/1", "origin": "local-metadata", "scope_complete": True,
              "files_seen": 0, "limits_hit": False,
              "layers": {key: {"state": "unknown", "files": 0} for key in LAYERS}}
    entries_seen = 0
    stack = [(root, 0, None)]
    while stack:
        folder, depth, inherited = stack.pop()
        try:
            with os.scandir(folder) as children:
                for entry in children:
                    entries_seen += 1
                    if entries_seen > max_entries:
                        result["scope_complete"] = False
                        result["limits_hit"] = True
                        stack.clear()
                        break
                    if entry.name.startswith(".") or entry.name.casefold() in SKIP:
                        continue
                    info = entry.stat(follow_symlinks=False)
                    if stat.S_ISLNK(info.st_mode):
                        continue
                    layer = (layer_for(entry.name) if depth == 0 else inherited)
                    if stat.S_ISDIR(info.st_mode):
                        if depth >= max_depth:
                            result["scope_complete"] = False
                            result["limits_hit"] = True
                        else:
                            stack.append((Path(entry.path), depth + 1, layer))
                    elif stat.S_ISREG(info.st_mode):
                        result["files_seen"] = min(MAX_FILES, result["files_seen"] + 1)
                        if depth == 0 and entry.name.casefold() in ROOT_FILES:
                            layer = "constitution"
                        if layer:
                            item = result["layers"][layer]
                            item["files"] = min(MAX_FILES, item["files"] + 1)
                            item["state"] = "found"
        except OSError:
            result["scope_complete"] = False
    for item in result["layers"].values():
        if item["state"] != "found" and result["scope_complete"]:
            item["state"] = "not_found"
    return result


def main():
    parser = argparse.ArgumentParser(description="Inspect structure locally; never read contents or upload data.")
    parser.add_argument("--root", required=True, help="A folder explicitly selected by its owner")
    args = parser.parse_args()
    try:
        print(json.dumps(scan(args.root), indent=2))
    except (ValueError, OSError):
        parser.exit(2, "Could not inspect the selected folder. No report was produced.\n")


if __name__ == "__main__":
    main()
