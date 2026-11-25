#!/usr/bin/env python3
"""Compare user-checked transcription fields with candidate readings offline."""

import argparse
import json
import unicodedata
from pathlib import Path


def unique_object(pairs):
    result = {}
    for name, value in pairs:
        if name in result:
            raise ValueError(f"duplicate JSON key {name!r}")
        result[name] = value
    return result


def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, ValueError) as error:
        raise ValueError(f"{path}: {error}") from error


def normalize(value):
    return " ".join(unicodedata.normalize("NFC", value).split())


def valid_id(value):
    return isinstance(value, str) and bool(value) and value == value.strip()


def read_checked(path):
    rows = load_json(path)
    if not isinstance(rows, list) or not rows:
        raise ValueError(f"{path}: expected a non-empty array of checked fields")

    checked = {}
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict) or set(row) != {"id", "expected"}:
            raise ValueError(f"{path}: checked field {index} must contain id and expected")

        field_id = row["id"]
        if not valid_id(field_id):
            raise ValueError(f"{path}: checked field {index} needs a non-blank id without outer whitespace")
        if field_id in checked:
            raise ValueError(f"{path}: duplicate checked id {field_id!r}")

        variants = row["expected"]
        if not isinstance(variants, list) or not variants or any(
            not isinstance(variant, str) or not normalize(variant) for variant in variants
        ):
            raise ValueError(f"{path}: {field_id!r} needs a non-empty list of non-blank strings")
        checked[field_id] = {normalize(variant) for variant in variants}
    return checked


def read_candidates(path):
    rows = load_json(path)
    if not isinstance(rows, dict):
        raise ValueError(f"{path}: expected an object mapping field ids to string or null")

    candidates = {}
    for field_id, value in rows.items():
        if not valid_id(field_id):
            raise ValueError(f"{path}: candidate id {field_id!r} is blank or has outer whitespace")
        if value is not None and not isinstance(value, str):
            raise ValueError(f"{path}: candidate {field_id!r} must be a string or null")
        candidates[field_id] = normalize(value) if value is not None else ""
    return candidates


def score(checked, candidates):
    counts = {"match": 0, "mismatch": 0, "missing": 0}
    fields = []
    for field_id, expected in checked.items():
        reading = candidates.get(field_id)
        if not reading:
            status = "missing"
        elif reading in expected:
            status = "match"
        else:
            status = "mismatch"
        counts[status] += 1
        fields.append({"id": field_id, "status": status})

    return {
        "checked_fields": len(checked),
        **counts,
        "match_percent": round(100 * counts["match"] / len(checked), 2),
        "fields": fields,
        "unscored_candidate_ids": sorted(candidates.keys() - checked.keys()),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checked", type=Path, help="JSON array of checked ids and expected variants")
    parser.add_argument("candidate", type=Path, help="JSON object of candidate values keyed by id")
    args = parser.parse_args()

    try:
        result = score(read_checked(args.checked), read_candidates(args.candidate))
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
