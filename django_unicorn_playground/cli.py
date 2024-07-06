from pathlib import Path

import click

from django_unicorn_playground.components import get_component_class_ast, get_component_class_import


@click.command()
@click.argument("component", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.version_option()
def cli(component: Path):
    component_path = component

    component_class = get_component_class_ast(component_path)
    # component_class = get_component_class_import(component_path)

    # Import here to avoid partially initialized module
    from django_unicorn_playground import UnicornPlayground

    UnicornPlayground().runserver(component_class)
