from click.testing import CliRunner

from django_unicorn_playground.cli import cli


def test_invalid_component_path():
    runner = CliRunner(mix_stderr=False)

    result = runner.invoke(
        cli,
        [
            "tests/invalid_component_path.py",
        ],
    )

    assert result.exit_code == 2
    assert "Invalid value for 'COMPONENT'" in result.stderr


def test_no_component_classes():
    runner = CliRunner()

    result = runner.invoke(
        cli,
        [
            "tests/__init__.py",
        ],
    )

    assert result.exit_code == 1
    assert "No subclass of UnicornView found" in str(result.exception)
