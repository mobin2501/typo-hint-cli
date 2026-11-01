import pytest

from typo_match import suggest

COMMANDS = ["commit", "push", "pull", "status", "stash"]


def test_swapped_letters_count_as_one_edit():
    assert suggest("stauts", COMMANDS, 1) == ["status"]


def test_closest_first_then_alphabetical():
    assert suggest("stas", COMMANDS, 2) == ["stash", "status"]  # distance 1, then 2
    assert suggest("pusl", COMMANDS, 1) == ["pull", "push"]  # both distance 1


def test_nothing_beyond_max_distance():
    assert suggest("deploy", COMMANDS, 1) == []


def test_exact_match_has_distance_zero():
    assert suggest("push", COMMANDS, 0) == ["push"]


def test_negative_max_distance_is_rejected():
    with pytest.raises(ValueError):
        suggest("push", COMMANDS, -1)
