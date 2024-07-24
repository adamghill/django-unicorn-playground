from unittest.mock import ANY

from django_unicorn_playground.settings import get_settings

from ..fake_components import FakeView


def test_get_settings():
    expected = {
        "ALLOWED_HOSTS": "*",
        "ROOT_URLCONF": ANY,
        "SECRET_KEY": ANY,
        "DEBUG": True,
        "TEMPLATES": ANY,
        "INSTALLED_APPS": ("django.contrib.staticfiles", "django_unicorn", "django_unicorn_playground"),
        "UNICORN": {"COMPONENTS": {}},
        "STATIC_URL": "static/",
    }
    actual = get_settings(template_dir=None, component_classes=[])

    assert expected == actual


def test_get_settings_component_classes():
    expected = {
        "ALLOWED_HOSTS": "*",
        "ROOT_URLCONF": ANY,
        "SECRET_KEY": ANY,
        "DEBUG": True,
        "TEMPLATES": ANY,
        "INSTALLED_APPS": ("django.contrib.staticfiles", "django_unicorn", "django_unicorn_playground"),
        "UNICORN": {"COMPONENTS": {"tests.fake_components": FakeView}},
        "STATIC_URL": "static/",
    }

    actual = get_settings(template_dir=None, component_classes=[FakeView])

    assert expected == actual
