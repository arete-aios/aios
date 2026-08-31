# Brief and decision-list contract

The brief prevents creative guesses. The decision list prevents technical guesses. Both are small, durable, and written before the render becomes expensive.

## One combined brief request

Ask for missing fields together, not as a chain of interruptions:

```text
Who is this for and where will it be shown?
What should the viewer understand or do, and what target length do you want?
Which aspect ratio or framing do you prefer, and should captions be burned in, delivered separately, or both?
May the footage use cloud tools, and is it approved for publication or private editing only?
Which editing app and version must open the timeline?
```

Record the answer with these fields:

```yaml
audience:
destination:
purpose:
target_length:
framing:
captions:
language:
cloud_processing: approved | local_only | not_set
publication: approved | private_not_approved | not_set
target_editor:
target_editor_version:
success_check:
```

If publication is not approved, local work may continue under `private_not_approved`. Upload cannot.

## Minimum decision-list fields

`edl.json` is the shared contract between render and editable timeline. It needs enough information to reproduce timing and layout without reading a previous chat.

```json
{
  "schema_version": "1.0",
  "project": {
    "time_base": "1/30000",
    "output_frame_rate": "30000/1001",
    "frame_rate_policy": "cfr_mezzanine",
    "target_editor": "named by owner",
    "target_editor_version": "named by owner",
    "timeline_validation_status": "import_unverified",
    "publication": "private_not_approved"
  },
  "sources": [
    {
      "id": "camera_a",
      "original_name": "camera identifier",
      "archive_path": "sources/camera-identifier_tag.mov",
      "sha256": "hex digest",
      "source_time_base": "1/600",
      "frame_rate_mode": "vfr",
      "edit_time_domain": "mezzanine",
      "mezzanine_path": "work/camera-identifier_cfr.mov",
      "mezzanine_sha256": "hex digest",
      "mezzanine_command": "recorded command or preset identifier",
      "time_mapping": "source and mezzanine start at the same presentation timestamp"
    }
  ],
  "regions": [
    {
      "id": "r1",
      "source_id": "camera_a",
      "time_domain": "mezzanine",
      "source_start": "3003/30000",
      "source_duration": "9009/30000",
      "output_start": "0/30000",
      "transform": {"scale": 1.0, "x": 0, "y": 0, "crop": null},
      "audio": {"gain_db": 0, "fade_in_ms": 0, "fade_out_ms": 80}
    }
  ],
  "captions": {
    "source": "out/captions.srt",
    "delivery": "burned_in_and_sidecar",
    "style_preset": "named preset"
  },
  "overlays": [
    {
      "id": "title_1",
      "asset": "out/assets/title_1.png",
      "parent_region_id": "r1",
      "start": "600/30000",
      "duration": "2400/30000"
    }
  ],
  "render_preset": {
    "name": "destination preset",
    "canvas": "1080x1350",
    "codec": "h264",
    "loudness_lufs": null,
    "true_peak_dbtp": null,
    "colour": "recorded input-to-output transform"
  }
}
```

Rational times are strings so different tools do not round them differently. The exact denominator may change, but it must be stated once and used consistently. Every region also names whether its times refer to the original or mezzanine domain; a mezzanine records its hash, generation command or preset, and timestamp mapping.

## Required validations

- Every `source_id` resolves and its archived bytes match the stored hash.
- VFR sources name either a CFR mezzanine mapping or an original-timestamp policy.
- Regions are ordered, non-negative, and inside their source extent.
- Overlay parent IDs exist and their times fall inside the parent region.
- Caption and overlay assets resolve from the package.
- Render and timeline read the same decision-list version.
- Timeline status is one of `schema_validated`, `import_tested`, or `import_unverified`; only the second proves the named editor opened it.
- Rights, cloud-processing status, editor target, and render preset are not blank at delivery.
