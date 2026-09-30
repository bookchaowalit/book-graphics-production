# Upgrade Plan

## Current state

Score: 6/10 (was 5/10) — small, typed and well-tested template renderer, but
it is an older fork of the graphics module that `book-production-platform`
now owns (recipe `template-batch-v2` here vs `v3` there, no print export), and
fixes must currently be made twice.

## Backlog

### P0

- Confirm the first GitHub Actions run is green, especially the PNG tests that
  use the runner's preinstalled Google Chrome.
- Decide ownership: either make this repository the single owner and have the
  platform depend on it, or archive it in favour of
  `book-production-platform/src/book_production_platform/graphics_production`.

### P1

- Batches write `<request_id>.svg/.png` straight into the shared output
  directory, so a later batch (different idempotency key) with the same
  `request_id` overwrites files an earlier manifest still hashes. Scope
  artifacts per batch or refuse to overwrite differing bytes.
- `run_batch` calls `raw.get(...)` on every item, so a non-object item in the
  batch raises `AttributeError` instead of an item-level rejection.

### P2

- Replace `httpx`-backed `fastapi.testclient` usage before Starlette drops it.

## Done in this pass

- Fixed: two items whose `request_id`s sanitize to the same file name
  (duplicates, case variants, stripped punctuation) overwrote each other's
  artifacts and broke the manifest hashes; the later item is now rejected with
  `artifact_name_collision` (same fix as the platform repository).
- PNG-rendering tests are marked `browser` and skip with a reason when no
  Chromium-family browser is installed (was 9 failures on such hosts); added
  browser-free naming tests.
- Added `.github/workflows/ci.yml` running `scripts/check.py` on Python 3.11
  and 3.12, and ignored generated `*.egg-info/`.
