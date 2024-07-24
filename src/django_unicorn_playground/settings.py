from os import getcwd
from pathlib import Path
from typing import Any
from uuid import uuid4

from django_unicorn.components import UnicornView
from typeguard import typechecked

from django_unicorn_playground import urls


@typechecked
def _get_components_setting(component_classes: list[type[UnicornView]]) -> dict[str, type[UnicornView]]:
    """Gets the `UNICORN.COMPONENTS` Django settings."""

    components = {}

    for component_class in component_classes:
        component_name = component_class.__module__
        components[component_name] = component_class

    return components


@typechecked
def _get_templates_setting(template_dir: Path | str | None = None) -> list[dict[str, Any]]:
    """Gets the `TEMPLATES` Django settings."""

    template_dirs = [getcwd()]

    if template_dir:
        template_dirs.append(str(template_dir))

    templates = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": template_dirs,
            "APP_DIRS": True,
            "OPTIONS": {
                "builtins": [
                    "django_unicorn.templatetags.unicorn",
                ],
            },
        },
    ]

    return templates


@typechecked
def get_settings(template_dir: Path | str | None, component_classes: list[type[UnicornView]]) -> dict[str, Any]:
    return {
        "ALLOWED_HOSTS": "*",
        "ROOT_URLCONF": urls,
        "SECRET_KEY": str(uuid4()),
        "DEBUG": True,
        "TEMPLATES": _get_templates_setting(template_dir),
        "INSTALLED_APPS": (
            "django.contrib.staticfiles",  # required for django-unicorn JavaScript
            "django_unicorn",
            "django_unicorn_playground",
        ),
        "UNICORN": {
            "COMPONENTS": _get_components_setting(component_classes),
        },
        "STATIC_URL": "static/",  # required for django-unicorn JavaScript
    }
