import os
from pathlib import Path
from typing import Any
from uuid import uuid4

from django import conf
from django.core.management import execute_from_command_line
from django_unicorn.components import UnicornView
from typeguard import typechecked

from django_unicorn_playground import urls
from django_unicorn_playground.components import get_component_classes

BASE_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@typechecked
class UnicornPlayground:
    def __init__(
        self,
        component_path: Path | str,
        template_dir: str | None = None,
        *args,  # noqa: ARG002
        **kwargs,
    ):
        self.template_dir = template_dir
        self.component_classes = get_component_classes(component_path)

        # Get default Django settings
        self.settings = self._get_settings()

        # Override default settings with the UnicornPlayground kwargs
        self.settings.update(**kwargs)

        # Set Django settings
        conf.settings.configure(**self.settings)

    def _get_components_setting(self) -> dict[str, type[UnicornView]]:
        """Gets the `UNICORN.COMPONENTS` Django settings."""

        components = {}

        for component_class in self.component_classes:
            component_name = component_class.__module__
            components[component_name] = component_class

        return components

    def _get_templates_setting(self) -> list[dict[str, Any]]:
        """Gets the `TEMPLATES` Django settings."""

        template_dirs = []

        if self.template_dir is not None:
            template_dirs.append(self.template_dir)

        templates = [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": template_dirs,
                "APP_DIRS": True,
            },
        ]

        return templates

    def _get_settings(self) -> dict[str, Any]:
        return {
            "ALLOWED_HOSTS": "*",
            "ROOT_URLCONF": urls,
            "SECRET_KEY": str(uuid4()),
            "DEBUG": True,
            "TEMPLATES": self._get_templates_setting(),
            "INSTALLED_APPS": (
                "django.contrib.staticfiles",  # required for django-unicorn JavaScript
                "django_unicorn",
                "django_unicorn_playground",
            ),
            "UNICORN": {
                "COMPONENTS": self._get_components_setting(),
            },
            "STATIC_URL": "static/",  # required for django-unicorn JavaScript
        }

    def runserver(self, *, port: int = 8000):
        """Starts the dev server."""

        execute_from_command_line(["manage", "runserver", str(port)])
