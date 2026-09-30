# Book Graphics Production

> **Ownership:** graphics production is owned by
> `book-production-platform` (`src/book_production_platform/graphics_production`
> and `graphics_ir`). This repository is a frozen fork kept until it is
> archived: safety fixes are mirrored here, new features are not. Run
> `python scripts/graphics_fork_parity.py --fork ..\book-graphics-production`
> in the platform repository to see which modules have drifted.

Book Graphics Production is a local-first tool for turning validated JSON
requests into editable SVG artwork and PNG previews. Its V1A templates are
`quote_card`, `product_card`, and `announcement`, each with square, portrait,
and story recipes. The normal path is deterministic and reports
`model_calls=0`; image generation and brief interpretation are outside V1A.

## Install and check

Use Python 3.11 or newer and install Microsoft Edge or Google Chrome for
headless SVG-to-PNG rendering. The browser is used locally for proper Thai
complex-script shaping; the product never sends artwork to a remote service.
Install the IR package and the API's development dependencies, then run the
repository check entrypoint:

```powershell
python -m pip install -e .\packages\graphics-production-ir
python -m pip install -e ".\services\graphics-production-api[dev]"
python .\scripts\check.py
```

## Build a batch

```powershell
python -m graphics_production.cli batch --input .\services\graphics-production-api\examples\batch.json --output .\.runtime\graphics-production --idempotency-key demo-1
```

The product accepts local assets and fonts beneath the selected asset root. It
rejects URL, traversal, unsafe SVG, and missing-file references; it does not
fetch network resources. Custom TTF/OTF files are embedded in SVG outputs under
a content-derived family name, so those files carry the supplied font data.
Outputs include editable SVG, PNG preview, QA results, and a replay-safe
manifest. Set `GRAPHICS_PRODUCTION_BROWSER` to choose a non-default Edge or
Chrome executable; `GRAPHICS_PRODUCTION_BROWSER_PROFILE` can relocate the
isolated local browser profile.

Artifacts are named after each item's `request_id` inside the output
directory. A later batch that would replace one of those files with different
bytes is rejected per item with `artifact_exists_with_different_content`, so an
earlier manifest's hashes stay valid; use a new output directory or
`request_id` for a changed render. Because browser PNG bytes can differ run to
run, reusing a `request_id` across batches may be rejected here even for the
same input; `book-production-platform` (the owner) avoids this with per-batch
artifact folders.

Run the 30-output synthetic benchmark:

```powershell
python -m graphics_production.scripts.benchmark --fixture .\services\graphics-production-api\tests\fixtures\batch_30.json --output-dir .\.runtime\graphics-v1a-benchmark
```

Inspect generated PNGs against the visual invariants in
[`tests/golden/README.md`](services/graphics-production-api/tests/golden/README.md).
The benchmark and golden set contain synthetic content only.
