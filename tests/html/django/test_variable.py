from django_unicorn_playground.html.django import variable


def test_variable_str():
    expected = "{{ asdf }}"
    actual = variable("asdf")

    assert expected == actual


def test_variable_int():
    expected = "{{ 1 }}"
    actual = variable(1)

    assert expected == actual


def test_variable_none():
    expected = ""
    actual = variable(None)

    assert expected == actual
