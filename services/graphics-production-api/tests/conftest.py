import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
PACKAGE_ROOT = REPO_ROOT / "packages" / "graphics-production-ir"
SERVICE_ROOT = REPO_ROOT / "services" / "graphics-production-api"
for path in (PACKAGE_ROOT, SERVICE_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
