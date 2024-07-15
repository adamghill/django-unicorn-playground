import os
from pathlib import Path

from django import conf
from django.core.management import execute_from_command_line
from typeguard import typechecked

from django_unicorn_playground.components import get_component_classes
from django_unicorn_playground.settings import get_settings

BASE_PATH = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@typechecked
class UnicornPlayground:
    def __init__(
        self,
        component_path: Path | str,
        *,
        template_dir: str | None = None,
        **django_settings,
    ):
        """
        Initialize a new playground.

        Args:
            component_path: Where the component lives on the filesystem.
            template_dir: Used to specify a template directory.
            django_settings: Override the default Django settings.
        """

        component_classes = get_component_classes(component_path)

        # Get default Django settings
        settings = get_settings(template_dir, component_classes)

        # Override default settings with any init kwargs
        settings.update(**django_settings)

        # Set Django settings
        conf.settings.configure(**settings)

    def runserver(self, *, port: int = 8000):
        """Starts the dev server.

        Args:
            port: The port that the dev server should be run on.
        """

        execute_from_command_line(["manage", "runserver", str(port)])