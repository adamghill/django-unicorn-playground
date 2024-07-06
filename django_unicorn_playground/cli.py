import click

from django_unicorn_playground.main import UnicornPlayground


@click.version_option()
def cli():
    UnicornPlayground().runserver()
