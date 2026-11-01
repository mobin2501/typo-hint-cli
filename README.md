# typo-hint-cli

A small command-line tool with git-style commands (`status`, `push`,
`commit`, ...). The known commands are listed in `commands.csv`.

```
$ python tool.py status
Running 'status'.

$ python tool.py stauts
tool: 'stauts' is not a command.
```

`typo_match.py` has `suggest(typed, commands, max_distance)`, which returns the
commands within `max_distance` edits of a mistyped word (Damerau-Levenshtein
distance via [rapidfuzz](https://github.com/rapidfuzz/RapidFuzz)), closest
first, ties broken alphabetically.

## Project layout

| Path | What it is |
|---|---|
| `tool.py` | The command-line tool; loads and checks `commands.csv` |
| `commands.csv` | The command list (35 commands) |
| `typo_match.py` | Typo matching (Damerau-Levenshtein) |
| `tests/` | pytest suite |

## Setup

Python 3.12:

```
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Run

```
.venv/bin/python tool.py <command>
```

Exit code 0 for a known command, 1 otherwise.

## Tests

```
.venv/bin/python -m pytest
```

## License

MIT
