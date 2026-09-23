"""Run the owner-repository tests and static checks on any supported OS."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IR_ROOT = ROOT / "packages" / "graphics-production-ir"
API_ROOT = ROOT / "services" / "graphics-production-api"


def main() -> int:
    env = os.environ.copy()
    import_paths = [str(IR_ROOT), str(API_ROOT)]
    env["PYTHONPATH"] = os.pathsep.join(
        [*import_paths, env["PYTHONPATH"]] if env.get("PYTHONPATH") else import_paths
    )
    env["MYPYPATH"] = os.pathsep.join(
        [str(IR_ROOT), env["MYPYPATH"]] if env.get("MYPYPATH") else [str(IR_ROOT)]
    )
    commands = (
        [sys.executable, "-m", "pytest", "packages/graphics-production-ir/tests", "services/graphics-production-api/tests", "-q"],
        [sys.executable, "-m", "ruff", "check", "packages/graphics-production-ir", "services/graphics-production-api"],
        [sys.executable, "-m", "mypy", "--strict", "services/graphics-production-api/graphics_production", "packages/graphics-production-ir/graphics_ir"],
    )
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, env=env, check=False)
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
