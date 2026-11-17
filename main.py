#!/usr/bin/env python3
"""ai-judge-rich-01 entry.

Writes one plan to /output/entry.txt: the plan an AI agent would follow, from
$100 in a wallet, a computer with internet access and 30 days, to the most
money it can hold on day 30.

The plan lives in plan.txt beside this file. It is read relative to __file__
because the grader runs `python3 -P -s /bot/main.py` from a working directory
that is not /bot, and -P keeps /bot off sys.path.

Bytes, not text mode. Text mode would translate line ends to the platform's
own and pick its own encoding; the judge reads the exact bytes written.
"""

from __future__ import annotations

import os
from pathlib import Path

PLAN_FILE = "plan.txt"
MIN_CHARS = 1
MAX_CHARS = 1000


def load_plan() -> bytes:
    """Return the plan exactly as it is stored, with no re-encoding.

    The three gate rules are checked here, on the bytes that will be written,
    so a mangled plan.txt fails in front of me instead of in front of the
    scorer: UTF-8, 1 to 1000 code points, and not only white space.
    """
    raw = (Path(__file__).resolve().parent / PLAN_FILE).read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"{PLAN_FILE} is not UTF-8: {exc}") from None

    count = len(text)  # Python counts code points, which is what the gate counts
    if not MIN_CHARS <= count <= MAX_CHARS:
        raise SystemExit(f"{PLAN_FILE} is {count} characters, the gate wants 1-1000")
    if not text.strip():
        raise SystemExit(f"{PLAN_FILE} is only white space")
    if "\r" in text:
        raise SystemExit(f"{PLAN_FILE} holds a carriage return, which the platform would translate")
    return raw


def output_dir() -> Path:
    """MAKEFUN_OUTPUT_DIR stands in for /output outside the grader."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return Path(override) if override else Path("/output")


def main() -> int:
    data = load_plan()
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    with open(target, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    # Read back what the judge will read: if these bytes differ, say so now.
    if target.read_bytes() != data:
        raise SystemExit(f"{target} does not hold the plan that was written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
