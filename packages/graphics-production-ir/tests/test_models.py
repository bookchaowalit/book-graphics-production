import pytest
from graphics_ir import GraphicRequest
from pydantic import ValidationError


def valid_request(**overrides: object) -> dict[str, object]:
    request: dict[str, object] = {
        "request_id": "quote-001",
        "template_id": "quote_card",
        "variant": "square",
        "canvas": {"width": 1080, "height": 1080, "background": "#FFFFFF"},
        "brand": {"primary": "#14213D", "accent": "#FCA311", "foreground": "#111111"},
        "content": {"quote": "ทำให้เรื่องยากชัดเจนขึ้น", "author": "Solo Empire"},
    }
    request.update(overrides)
    return request


def test_graphic_request_accepts_typed_v1_contract() -> None:
    request = GraphicRequest.model_validate(valid_request())

    assert request.schema_version == "graphic-request.v1"
    assert request.template_id == "quote_card"
    assert request.content["quote"] == "ทำให้เรื่องยากชัดเจนขึ้น"


def test_graphic_request_rejects_unknown_template() -> None:
    with pytest.raises(ValidationError):
        GraphicRequest.model_validate(valid_request(template_id="freeform"))


@pytest.mark.parametrize("dimensions", [(0, 1080), (-1, 1080), (1080, 0), (1080, 5000)])
def test_graphic_request_rejects_invalid_dimensions(dimensions: tuple[int, int]) -> None:
    with pytest.raises(ValidationError):
        GraphicRequest.model_validate(valid_request(canvas={"width": dimensions[0], "height": dimensions[1]}))
