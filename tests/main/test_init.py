from unittest.mock import ANY

import pytest

from django_unicorn_playground.main import UnicornPlayground


@pytest.fixture
def playground_settings():
    return {
        "ALLOWED_HOSTS": "*",
        "ROOT_URLCONF": ANY,
        "SECRET_KEY": ANY,
        "DEBUG": True,
        "TEMPLATES": [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": ANY,
                "APP_DIRS": True,
                "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
            }
        ],
        "INSTALLED_APPS": ("django.contrib.staticfiles", "django_unicorn", "django_unicorn_playground"),
        "UNICORN": {"COMPONENTS": {"fake_components": ANY}},
        "STATIC_URL": "static/",
    }.copy()


def test_init_no_component_path():
    with pytest.raises(TypeError) as e:
        UnicornPlayground()

    assert (
        e.exconly()
        == "TypeError: UnicornPlayground.__init__() missing 1 required positional argument: 'component_path'"
    )


def test_init(monkeypatch, playground_settings):
    monkeypatch.setattr("django_unicorn_playground.main.UnicornPlayground.configure", lambda s: None)

    actual = UnicornPlayground("tests/fake_components.py")

    assert playground_settings == actual.settings


def test_init_template_dir(monkeypatch, playground_settings):
    monkeypatch.setattr("django_unicorn_playground.settings.getcwd", lambda: "/test")
    monkeypatch.setattr("django_unicorn_playground.main.UnicornPlayground.configure", lambda s: None)

    playground_settings["TEMPLATES"][0]["DIRS"] = [
        "/test",
        "tests/templates",
    ]

    actual = UnicornPlayground("tests/fake_components.py", template_dir="tests/templates")

    assert playground_settings == actual.settings


def test_init_override_setting(monkeypatch, playground_settings):
    monkeypatch.setattr("django_unicorn_playground.main.UnicornPlayground.configure", lambda s: None)

    playground_settings["STATIC_URL"] = "/test"

    actual = UnicornPlayground("tests/fake_components.py", STATIC_URL="/test")

    assert playground_settings == actual.settings


def test_init_new_setting(monkeypatch, playground_settings):
    monkeypatch.setattr("django_unicorn_playground.main.UnicornPlayground.configure", lambda s: None)

    playground_settings["TEST_SETTING"] = "something-new"

    actual = UnicornPlayground("tests/fake_components.py", TEST_SETTING="something-new")

    assert playground_settings == actual.settings
