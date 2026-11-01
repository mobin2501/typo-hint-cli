from tool import main


def test_known_command_runs(capsys):
    assert main(["status"]) == 0
    assert capsys.readouterr().out == "Running 'status'.\n"


def test_unknown_command_fails(capsys):
    assert main(["stauts"]) == 1
    assert "tool: 'stauts' is not a command." in capsys.readouterr().err


def test_no_command_shows_usage(capsys):
    assert main([]) == 1
    assert "usage:" in capsys.readouterr().err


def test_command_list_is_loaded():
    from tool import COMMANDS

    assert len(COMMANDS) == 35
    assert "status" in COMMANDS


def test_broken_command_list_lists_every_problem(tmp_path):
    import pytest

    from tool import load_commands

    path = tmp_path / "commands.csv"
    path.write_text("command\npush\nPush\npush\n", encoding="utf-8")
    with pytest.raises(ValueError) as error:
        load_commands(path)
    assert "row 3: 'Push' is not a lower-case command" in str(error.value)
    assert "row 4: duplicate command 'push'" in str(error.value)
