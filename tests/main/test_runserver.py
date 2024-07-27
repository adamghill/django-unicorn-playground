from unittest.mock import patch

from django_unicorn_playground.main import UnicornPlayground


@patch("django_unicorn_playground.main.execute_from_command_line")
@patch("django_unicorn_playground.main.django_conf_settings")
def test_runserver(django_conf_settings, execute_from_command_line):
    UnicornPlayground("tests/fake_components.py").runserver()

    execute_from_command_line.assert_called_once_with(["manage", "runserver", "8000"])
