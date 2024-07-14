import os
from pathlib import Path

from django import conf
from django.core.management import execute_from_command_line
from django_unicorn.components import UnicornView

from django_unicorn_playground import urls

BASE_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class UnicornPlayground:
    def __init__(self, component_class: UnicornView, *args, **kwargs):
        self.component_class = component_class
        # TODO: Take kwargs and use them for Django settings ala `coltrane`

        templates = [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [BASE_PATH / "django_unicorn_playground/templates"],
                "APP_DIRS": True,
                "OPTIONS": {},
            },
        ]

        conf.settings.configure(
            ALLOWED_HOSTS="*",
            ROOT_URLCONF=urls,
            SECRET_KEY="asdf",  # TODO: Generate secret key
            DEBUG=True,  # TODO: Able to set this to False
            TEMPLATES=templates,  # TODO: Override template
            INSTALLED_APPS=(
                "django.contrib.staticfiles",
                "django_unicorn",
                "django_unicorn_playground",
            ),
            UNICORN={
                "APPS": (self.component_class.__module__,),
                "COMPONENTS": [
                    self.component_class,
                ],
            },
            STATIC_URL="static/",
        )

    def runserver(self, port: int = 8000):
        execute_from_command_line(["manage", "runserver", str(port)])
