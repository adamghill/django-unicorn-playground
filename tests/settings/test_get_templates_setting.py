from pathlib import Path
from unittest.mock import ANY

from django_unicorn_playground.settings import _get_templates_setting


def test_get_templates_setting():
    expected = [
        {
            "APP_DIRS": True,
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [ANY],
            "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
        }
    ]
    actual = _get_templates_setting()

    assert expected == actual


def test_get_templates_setting_cwd(monkeypatch):
    monkeypatch.setattr("django_unicorn_playground.settings.getcwd", lambda: "/test")

    expected = [
        {
            "APP_DIRS": True,
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["/test"],
            "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
        }
    ]
    actual = _get_templates_setting()

    assert expected == actual


def test_get_templates_setting_template_dir_none(monkeypatch):
    monkeypatch.setattr("django_unicorn_playground.settings.getcwd", lambda: "/test")

    expected = [
        {
            "APP_DIRS": True,
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["/test"],
            "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
        }
    ]
    actual = _get_templates_setting(template_dir=None)

    assert expected == actual


def test_get_templates_setting_template_dir_str(monkeypatch):
    monkeypatch.setattr("django_unicorn_playground.settings.getcwd", lambda: "/test")

    expected = [
        {
            "APP_DIRS": True,
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["/test", "/test"],
            "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
        }
    ]
    actual = _get_templates_setting(template_dir="/test")

    assert expected == actual


def test_get_templates_setting_template_dir_path(monkeypatch):
    monkeypatch.setattr("django_unicorn_playground.settings.getcwd", lambda: "/test")

    expected = [
        {
            "APP_DIRS": True,
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": ["/test", "/test"],
            "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
        }
    ]
    actual = _get_templates_setting(template_dir=Path("/test"))

    assert expected == actual
