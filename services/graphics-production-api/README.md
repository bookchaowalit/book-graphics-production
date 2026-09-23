# Graphics Production API — V1A Template Batch

Graphics V1A turns validated JSON items into editable SVG plus PNG previews.
The standard path is deterministic: request → `GraphicIR` → fixed template →
SVG/PNG → QA. It supports `quote_card`, `product_card`, and `announcement`
with `square` (1080×1080), `portrait` (1080×1350), and `story` (1080×1920)
recipes.

No provider configuration or LLM is needed for layout. Every batch reports
`model_calls=0`; a future brief extractor, background segmentation step, or
new-asset generator must be a separate capability with its own budget and
validation contract.

Run a local batch:

```text
python -m graphics_production.cli batch --input examples/batch.json --output .runtime/graphics-production --idempotency-key demo-1
```

Run the 30-output benchmark:

```text
python -m graphics_production.scripts.benchmark --fixture tests/fixtures/batch_30.json --output-dir artifacts/graphics-v1a-benchmark
```

The API exposes `GET /health` and `POST /v1/graphics/batches`. Asset and font
references must be local files beneath `asset_root`; URL, traversal, unsafe SVG
and missing-file references are rejected before an artifact is written.
