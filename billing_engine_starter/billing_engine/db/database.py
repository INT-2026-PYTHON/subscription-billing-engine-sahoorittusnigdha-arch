"""
Database connection helper.

✅ COMPLETE. Use this from repositories; do not call sqlite3 directly elsewhere.

Usage:
    db = Database("billing.db")
    db.init_schema()                 # one-time setup
    with db.transaction() as conn:   # for multi-statement atomic work
        conn.execute("INSERT ...")
        conn.execute("INSERT ...")
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


    