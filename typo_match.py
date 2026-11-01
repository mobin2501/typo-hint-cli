"""Typo matching: find the commands closest to a mistyped word.

Uses Damerau-Levenshtein distance from rapidfuzz: the number of single-letter
edits (insert, delete, replace, or swap two neighbouring letters) needed to
turn one word into the other.
"""

from __future__ import annotations

from rapidfuzz.distance import DamerauLevenshtein


def suggest(typed: str, commands: list[str], max_distance: int) -> list[str]:
    """Return the commands at most max_distance edits away, closest first.

    Ties are broken alphabetically. An empty list means nothing is close enough.
    """
    if max_distance < 0:
        raise ValueError("max_distance must be 0 or more")
    scored = []
    for command in commands:
        distance = DamerauLevenshtein.distance(typed, command, score_cutoff=max_distance)
        if distance <= max_distance:
            scored.append((distance, command))
    scored.sort()
    return [command for _, command in scored]
