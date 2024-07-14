from pathlib import Path

import click

from django_unicorn_playground import UnicornPlayground


@click.command()
@click.argument("component_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--port", type=int, default=8000, help="Port for localhost")
@click.version_option()
def cli(component_path: Path, port: int):
    UnicornPlayground(component_path=component_path).runserver(port=port)
