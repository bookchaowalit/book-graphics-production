from graphics_ir import GraphicRequest, validate_request


def test_validate_request_reports_unsupported_variant() -> None:
    request = GraphicRequest.model_validate({
        "request_id": "a",
        "template_id": "announcement",
        "variant": "square",
        "canvas": {"width": 1080, "height": 1080},
        "brand": {"primary": "#000000", "accent": "#FFFFFF", "foreground": "#111111"},
        "content": {"headline": "ข่าวสาร"},
    })

    assert validate_request(request) == []


def test_validate_request_uses_actionable_issue_codes() -> None:
    issues = validate_request({
        "request_id": "",
        "template_id": "announcement",
        "variant": "story",
        "canvas": {"width": 1080, "height": 1080},
        "brand": {"primary": "#000000", "accent": "#FFFFFF", "foreground": "#111111"},
        "content": {},
    })

    assert {issue.code for issue in issues} >= {"request_id_required", "content_required"}
