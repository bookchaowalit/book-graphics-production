import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
PACKAGE_ROOT = REPO_ROOT / "packages" / "graphics-production-ir"
SERVICE_ROOT = REPO_ROOT / "services" / "graphics-production-api"
for path in (PACKAGE_ROOT, SERVICE_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import pytest
from graphics_production.render import _find_browser

BROWSER_SKIP = pytest.mark.skip(
    reason=(
        "a local Chromium-family browser is required for PNG rendering; "
        "install Edge/Chrome/Chromium or set GRAPHICS_PRODUCTION_BROWSER"
    )
)


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "browser: needs a local Chromium-family browser to rasterize PNGs")


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    if _find_browser() is not None:
        return
    for item in items:
        if item.get_closest_marker("browser"):
            item.add_marker(BROWSER_SKIP)
