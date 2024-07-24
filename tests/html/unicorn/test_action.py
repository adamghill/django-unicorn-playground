import pytest
import typeguard

from django_unicorn_playground.html.unicorn import action, blur, change, click, focus, input, submit


def fake_method():
    pass


def test_action():
    expected = {"unicorn:click": "test"}
    actual = action("click", "test")

    assert expected == actual


def test_action_method():
    expected = {"unicorn:click": "fake_method"}
    actual = action("click", fake_method)

    assert expected == actual


def test_input():
    expected = {"unicorn:input": "test"}
    actual = input("test")

    assert expected == actual


def test_focus():
    expected = {"unicorn:focus": "test"}
    actual = focus("test")

    assert expected == actual


def test_change():
    expected = {"unicorn:change": "test"}
    actual = change("test")

    assert expected == actual


def test_blur():
    expected = {"unicorn:blur": "test"}
    actual = blur("test")

    assert expected == actual


def test_submit():
    expected = {"unicorn:submit": "test"}
    actual = submit("test")

    assert expected == actual


def test_click():
    expected = {"unicorn:click": "test"}
    actual = click("test")

    assert expected == actual


def test_action_invalid_event():
    with pytest.raises(typeguard.TypeCheckError):
        action("asdf", "test")
