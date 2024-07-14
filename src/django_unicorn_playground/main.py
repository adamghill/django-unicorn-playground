import os
from pathlib import Path

from django import conf
from django.core.management import execute_from_command_line

from django_unicorn_playground import urls
from django_unicorn_playground.components import get_component_class_import

BASE_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UnicornPlayground:
    def __init__(
        self,
        component_path: Path | str,
        component_name: str | None = None,
        components: dict | None = None,
        template_dir: str | None = None,
        *args,  # noqa: ARG002
        **kwargs,
    ):
        if isinstance(component_path, str):
            component_path = Path(component_path)

        self.component_class = get_component_class_import(component_path)

        template_dirs = []

        if template_dir is not None:
            template_dirs.append(template_dir)

        templates = [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": template_dirs,
                "APP_DIRS": True,
            },
        ]

        self.component_name = component_name or self.component_class.__module__

        if components is None:
            components = {}

        self.components = components or {
            self.component_name: self.component_class,
        }

        settings = {
            "ALLOWED_HOSTS": "*",
            "ROOT_URLCONF": urls,
            "SECRET_KEY": "asdf",  # TODO: Generate secret key
            "DEBUG": True,  # TODO: Able to set this to False
            "TEMPLATES": templates,  # TODO: Override template
            "INSTALLED_APPS": (
                "django.contrib.staticfiles",
                "django_unicorn",
                "django_unicorn_playground",
            ),
            "UNICORN": {
                "COMPONENTS": self.components,
            },
            "STATIC_URL": "static/",
        }
        settings.update(**kwargs)

        conf.settings.configure(**settings)

    def runserver(self, *, port: int = 8000):
        execute_from_command_line(["manage", "runserver", str(port)])
