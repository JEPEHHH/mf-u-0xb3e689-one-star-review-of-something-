#!/usr/bin/env python3
"""Local checks for the entry, mirroring the competition's written gate.

The gate (competition.yaml / RULES.txt): /output/entry.txt is UTF-8 text of 1 to
160 characters, not only white space. The judge additionally wants one single line.
This script runs the entrypoint in a throwaway output directory and asserts every
one of those, plus determinism (the grader runs the entry twice and compares the
outputs byte for byte).

Run:  python3 tests/test_entry.py
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def load_main():
    spec = importlib.util.spec_from_file_location("entry_main", REPO / "main.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_entrypoint(out_dir: Path) -> bytes:
    """Run main.py exactly as the harness would, with the output dir overridden."""
    env = {"PATH": "/usr/bin:/bin", "MAKEFUN_OUTPUT_DIR": str(out_dir)}
    proc = subprocess.run(
        [sys.executable, "main.py"],
        cwd=REPO,
        env=env,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"entrypoint exited {proc.returncode}: {proc.stderr}"
    return (out_dir / "entry.txt").read_bytes()


def check_gate(raw: bytes) -> str:
    text = raw.decode("utf-8")  # a UnicodeDecodeError here fails the check
    assert 1 <= len(text) <= 160, f"length {len(text)} outside 1..160"
    assert text.strip() != "", "text is only white space"
    assert "\n" not in text and "\r" not in text, "more than one line"
    return text


def main() -> int:
    module = load_main()

    with tempfile.TemporaryDirectory() as tmp:
        raw_a = run_entrypoint(Path(tmp) / "a")
        raw_b = run_entrypoint(Path(tmp) / "b")

    text = check_gate(raw_a)

    # Deterministic: the grader's two runs must write the same bytes.
    assert raw_a == raw_b, "the entry is not deterministic across runs"

    # The file is exactly the review the source declares, with no trailing newline.
    assert raw_a.decode("utf-8") == module.REVIEW, "entry.txt differs from main.py REVIEW"
    assert not raw_a.endswith(b"\n"), "entry.txt carries a trailing newline"

    # Byte count equals character count (pure ASCII), which keeps the size tie-break low.
    assert len(raw_a) == len(text), "bytes and characters differ"

    # Entrypoint shape the harness requires: main.py at the root, and no main.ts.
    assert (REPO / "main.py").is_file(), "main.py missing at the repository root"
    assert not (REPO / "main.ts").exists(), "main.ts present as well as main.py"

    # The programme must not depend on the network or on secrets: it reads no URL,
    # no environment value it needs, and writes only entry.txt.
    src = (REPO / "main.py").read_text(encoding="utf-8")
    for forbidden in ("http://", "https://", "requests", "urllib", "socket", "subprocess"):
        assert forbidden not in src, f"main.py mentions {forbidden!r}"

    print("all gate checks passed")
    print(f"  text  : {text}")
    print(f"  chars : {len(text)}  bytes: {len(raw_a)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
