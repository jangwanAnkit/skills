#!/usr/bin/env python3
"""Wrapper to use opencode instead of claude for skill-creator scripts."""

import subprocess
import os
import json


def run_opencode_p(prompt: str, model: str | None = None, timeout: int = 300) -> str:
    """Run opencode run -p and return the text response."""
    cmd = ["opencode", "run", "-p"]
    if model:
        cmd.extend(["-m", model])

    # Filter environment
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE",)}

    result = subprocess.run(
        cmd,
        input=prompt,
        capture_output=True,
        text=True,
        env=env,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"opencode run -p exited {result.returncode}\nstderr: {result.stderr}"
        )

    # Filter out ANSI codes and status lines
    lines = result.stdout.split("\n")
    filtered_lines = []
    for line in lines:
        # Skip ANSI escape codes and status lines
        if "\x1b[" in line:
            continue
        if line.strip() in ("", ">", "build · minimax-m2.5-free"):
            continue
        filtered_lines.append(line)

    return "\n".join(filtered_lines).strip()


if __name__ == "__main__":
    import sys

    prompt = sys.stdin.read()
    model = sys.argv[1] if len(sys.argv) > 1 else None
    print(run_opencode_p(prompt, model))
