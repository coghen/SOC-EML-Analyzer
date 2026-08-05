#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SOC – EML Analyzer. Loads gzip+base64 payload from data/payload.* files."""
from pathlib import Path
import gzip, base64, sys

ROOT = Path(__file__).resolve().parent
parts = []
for i in range(3):
    p = ROOT / "data" / f"payload.{i}"
    if not p.exists():
        sys.exit(f"Missing {p}")
    parts.append(p.read_text(encoding="ascii"))
code = gzip.decompress(base64.b64decode("".join(parts))).decode("utf-8")
g = {"__name__": "__main__", "__file__": str(ROOT / "app.py")}
exec(compile(code, str(ROOT / "app_full.py"), "exec"), g)
