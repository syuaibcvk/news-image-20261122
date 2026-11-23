#!/usr/bin/env python3
"""Deliver the front page of Sunday 22 November 2026.

This repository holds one picture, entry.png: a newspaper front page
that sums up the world news of Sunday 22 November 2026. It leads with
the collapse of the COP31 climate talks in Antalya — the longest UN
climate summit ever, ending with no deal and no mention of fossil
fuels — and continues with a Russian drone strike on a Kyiv apartment
block, a Russian warship sunk by sea drones off Benghazi, Iran's strike
on Bahrain, the Democrats' 258-seat House majority, the Nvidia SEC
probe, Trump's dare to Iran over the Hormuz blockade, settler arson in
the West Bank, the Houthi claim on the Rabigh refinery, drone strikes
on Khartoum, the capture of "El Chapo Isidro" in Sinaloa, South Korea's
education minister resigning over AI exam cheating, and the Cikande
candy-factory fire, with shorter briefs below.

The picture was drawn by render_frontpage.py (Pillow, deterministic,
no network), which lives in the workspace next to this repository, not
inside it. This program's whole job is to put that picture, unchanged,
at $MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output/entry.png).
It uses only the standard library, touches no network and reads no
clock, so every run writes exactly the same bytes. The bundled picture
is checked before delivery and the delivered copy is checked after it:
a file that is not a whole PNG, is over the 1 MiB cap, or differs from
the pinned picture by a single byte fails the run instead of passing
silently.
"""

import hashlib
import os
import sys
from pathlib import Path
from typing import NoReturn

REPO_DIR = Path(__file__).resolve().parent
SOURCE = REPO_DIR / "entry.png"

MAX_BYTES = 1_048_576  # the competition's 1 MiB limit
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# SHA-256 of entry.png as rendered by render_frontpage.py and frozen on
# 23 November 2026. Filled in after the final render; the stored picture
# must match it exactly, so a damaged or swapped entry.png is refused
# rather than delivered.
EXPECTED_SHA256 = "b342fef876f902bbba119ed4f1e234a690f2a2462f9f37806bc49c8f93e22f23"


def fail(message: str) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_entry() -> bytes:
    """Read the bundled picture and verify it end to end."""
    if not SOURCE.is_file():
        fail(f"bundled picture missing: {SOURCE}")
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        fail(f"bundled picture is {len(data)} bytes, over the 1 MiB cap")
    if not data.startswith(PNG_SIGNATURE):
        fail("bundled picture is not a PNG (bad signature)")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        fail("bundled picture does not match the pinned SHA-256")
    return data


def deliver(data: bytes) -> Path:
    """Write the verified bytes to the output directory and check the
    copy byte for byte."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        fail("delivered copy is not byte-identical to the bundled picture")
    return target


def main() -> None:
    data = load_entry()
    target = deliver(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
