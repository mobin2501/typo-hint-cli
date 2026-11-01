"""A small command-line tool with git-style commands.

Usage: python tool.py <command>

Known commands come from commands.csv next to this file.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

COMMANDS_FILE = Path(__file__).resolve().parent / "commands.csv"

# Lower-case letters, optionally joined by single hyphens, e.g. "push", "cherry-pick".
WORD_PATTERN = re.compile(r"^[a-z]+(?:-[a-z]+)*$")


def load_commands(path: Path) -> list[str]:
    """Read the command list and fail with every problem at once if it is broken."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["command"]:
            raise ValueError(f"{path}: expected a single 'command' column, got {reader.fieldnames}")
        commands = [row["command"] for row in reader]
    problems = []
    seen: set[str] = set()
    for n, command in enumerate(commands, 2):
        if not WORD_PATTERN.match(command):
            problems.append(f"row {n}: {command!r} is not a lower-case command")
        if command in seen:
            problems.append(f"row {n}: duplicate command {command!r}")
        seen.add(command)
    if not commands:
        problems.append("no commands")
    if problems:
        raise ValueError(f"{path}:\n  " + "\n  ".join(problems))
    return commands


COMMANDS = load_commands(COMMANDS_FILE)


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args:
        print("usage: python tool.py <command>", file=sys.stderr)
        return 1
    command = args[0]
    if command in COMMANDS:
        print(f"Running '{command}'.")
        return 0
    print(f"tool: '{command}' is not a command.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
