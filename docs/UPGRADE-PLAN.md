# Upgrade Plan

## Current state

Score: 6.5/10 (was 6/10 after pass 1, 5/10 before) — small, typed and
well-tested template renderer; ownership is now decided (the platform owns
graphics, this is a frozen fork), but safety fixes still have to be mirrored
until it is archived.

## Backlog

### P0

- Confirm the first GitHub Actions run is green, especially the PNG tests that
  use the runner's preinstalled Google Chrome.
- Archive this repository once no workflow uses it (the platform's
  `scripts/graphics_fork_parity.py` already shows nothing exists only here).
  Until then mirror only safety fixes, not features.

### P1

- Features missing vs the platform (Thai cluster-aware wrapping in `layout.py`,
  announcement layout for portrait/story, print export, per-batch artifact
  folders): do not port; point users at the platform instead.

### P2

- Replace `httpx`-backed `fastapi.testclient` usage before Starlette drops it.

## Done in pass 1

- Fixed: two items whose `request_id`s sanitize to the same file name
  (duplicates, case variants, stripped punctuation) overwrote each other's
  artifacts and broke the manifest hashes; the later item is now rejected with
  `artifact_name_collision` (same fix as the platform repository).
- PNG-rendering tests are marked `browser` and skip with a reason when no
  Chromium-family browser is installed (was 9 failures on such hosts); added
  browser-free naming tests.
- Added `.github/workflows/ci.yml` running `scripts/check.py` on Python 3.11
  and 3.12, and ignored generated `*.egg-info/`.

## Done in this pass (pass 2)

- Fixed (mirrored from the platform): a later batch with the same
  `request_id` silently overwrote SVG/PNG files an earlier manifest still
  hashes; such items are now rejected with
  `artifact_exists_with_different_content` (identical bytes are reused).
- Fixed: a non-object batch item raised `AttributeError` for the whole batch;
  it is now an item-level `invalid_request` rejection.
- Ownership decided and documented in the README: `book-production-platform`
  owns graphics; this repository is a frozen fork pending archive.

## Done in this pass (pass 3)

- Per-batch artifact folders (`<output>/<batch_id>/`, so a later batch whose
  PNG bytes differ is no longer rejected with
  `artifact_exists_with_different_content`) landed in the owner,
  `book-production-platform`. Deliberately not mirrored here: this fork's
  behaviour already fails closed (no data loss), and a manifest layout change
  is a feature, which this frozen fork does not take. The README now
  documents the limitation and points at the platform.
