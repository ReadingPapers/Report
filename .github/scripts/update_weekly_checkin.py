#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Insert a weekly placeholder entry after the anchor in 每周精读打卡.md.
- Anchor: "> ==> 时间倒序，本次更新插入位置 <=="
- Insert line (Markdown quoted): ">[YYYY-MM-DD]-[程浩]-[本周未精读]"
- Date uses Asia/Shanghai timezone for Wednesday 08:00 local run.
- Idempotent: if an identical entry already immediately follows the anchor for the same date, do nothing.
"""
from __future__ import annotations
import io
import os
import re
from datetime import datetime

try:
    # Python 3.9+
    from zoneinfo import ZoneInfo  # type: ignore
except Exception:  # pragma: no cover
    ZoneInfo = None  # type: ignore

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TARGET_FILE = os.path.join(REPO_ROOT, "每周精读打卡.md")
ANCHOR = "> ==> 时间倒序，本次更新插入位置 <=="
AUTHOR = "程浩"


def get_today_shanghai_str() -> str:
    if ZoneInfo is not None:
        tz = ZoneInfo("Asia/Shanghai")
        now = datetime.now(tz)
    else:  # Fallback to naive localtime
        now = datetime.now()
    return now.strftime("%Y-%m-%d")


def main() -> int:
    if not os.path.exists(TARGET_FILE):
        raise FileNotFoundError(TARGET_FILE)

    with io.open(TARGET_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    date_str = get_today_shanghai_str()
    # Decide blockquote prefix by inspecting following entries
    # Default to nested blockquote "> >" to match existing style
    quote_prefix = "> >"

    # Find anchor line position
    lines = content.splitlines()
    try:
        idx = lines.index(ANCHOR)
    except ValueError:
        # try to find trimmed match (in case of trailing spaces)
        idx = next((i for i, l in enumerate(lines) if l.strip() == ANCHOR.strip()), -1)
        if idx == -1:
            raise RuntimeError("Anchor not found in target file")

    # Determine insert position: after the anchor line
    insert_pos = idx + 1

    # If the immediate next line is a single blockquote marker (">" with optional spaces),
    # keep that empty line and insert after it for better readability.
    if insert_pos < len(lines) and lines[insert_pos].strip().rstrip() in {">", ">>"}:
        insert_pos += 1

    # Inspect the first non-empty (non-pure ">") entry after anchor to choose prefix
    for j in range(insert_pos, min(insert_pos + 5, len(lines))):
        s = lines[j].lstrip()
        if not s:
            continue
        if s.startswith("> >[") or s.startswith("> > ["):
            quote_prefix = "> >"
            break
        if s.startswith(">[") or s.startswith("> ["):
            quote_prefix = ">"
            break

    new_line = f"{quote_prefix}[{date_str}]-[{AUTHOR}]-[本周未精读]"

    # Skip any trailing spaces-only line after anchor? Keep exact structure.
    # Check if the line right after anchor already has the same entry today.
    if insert_pos < len(lines) and lines[insert_pos].strip() == new_line.strip():
        print("Entry for today already exists. No change.")
        return 0

    # If the next non-empty quoted line for AUTHOR with same date exists anywhere just after anchor, avoid duplicate.
    # But requirement says insert one entry right after the anchor. We'll insert regardless unless the immediate next line matches.

    # Insert the new line at insert_pos
    lines.insert(insert_pos, new_line)

    new_content = "\n".join(lines) + ("\n" if content.endswith("\n") else "")

    if new_content != content:
        with io.open(TARGET_FILE, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Inserted: {new_line}")
    else:
        print("No changes needed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
