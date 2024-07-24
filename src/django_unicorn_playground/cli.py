from pathlib import Path

import rich_click as click

from django_unicorn_playground import UnicornPlayground


@click.command()
@click.argument("component", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option("--port", type=int, default=8000, help="Port for the developer webserver.")
@click.option(
    "--template_dir", type=click.Path(exists=True, dir_okay=True, path_type=Path), help="Directory for templates."
)
@click.version_option()
def cli(component: Path, template_dir: Path, port: int):
    UnicornPlayground(component_path=component, template_dir=template_dir).runserver(port=port)
