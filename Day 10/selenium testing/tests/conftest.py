from __future__ import annotations

import socket
import subprocess
import time
from pathlib import Path
from typing import Iterator

import pytest
import requests


def _get_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return int(s.getsockname()[1])


@pytest.fixture(scope="session")
def server_url() -> Iterator[str]:
    """Start the local Flask app for testing."""
    port = _get_free_port()

    repo_root = Path(__file__).resolve().parents[3]
    venv_python = repo_root / ".venv" / "bin" / "python"
    app_path = repo_root / "Day 10" / "selenium testing" / "simple_site" / "app.py"

    env = {
        **{k: v for k, v in dict(**__import__("os").environ).items()},
        "PORT": str(port),
        "FLASK_SECRET_KEY": "test-secret",
    }

    proc = subprocess.Popen(
        [str(venv_python), str(app_path)],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    base = f"http://127.0.0.1:{port}"

    try:
        # Wait for server readiness
        deadline = time.time() + 15
        while time.time() < deadline:
            try:
                r = requests.get(f"{base}/health", timeout=0.5)
                if r.status_code == 200:
                    break
            except Exception:
                time.sleep(0.2)
        else:
            raise RuntimeError("Flask server did not start in time")

        yield base
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
