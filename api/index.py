"""Vercel entry point: the live API is the FastAPI app in sourcebound/api/app.py.

Vercel runs this file as one Python function; vercel.json rewrites /api/* here. The project root is put on
the import path so the sourcebound package is found however the function is started.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sourcebound.api.app import app  # noqa: E402

__all__ = ["app"]
