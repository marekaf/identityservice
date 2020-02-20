#!/usr/bin/env python3
"""
Command Line Interface for for registering and authenticating users
"""

import click
from . import identity_service as ids

@click.group()
@click.version_option()
def cli():
    """
    Simple CLI for registering and authenticating users
    """

# register
@cli.command()
@click.argument('username', type=click.STRING, required=True, metavar="username")
@click.argument('password', type=click.STRING, required=True, metavar="password")
@click.argument('properties', type=click.STRING, default="{}", metavar="properties")
@click.option('--file', '-f', type=click.Path(file_okay=True), default="users.json",
              help="File to persist the state.", required=True)
def register(username, password, properties, file):
    """Registers users."""
    is1 = ids.IdentityService()
    is1.load_to_json(file)
    is1.register(username, password, properties)
    is1.save_to_json(file, overwrite=True)

    info_msg = 'User registered. Database stored in ' + file
    click.echo(info_msg)

# authenticate
@cli.command()
@click.argument('username', type=click.STRING, required=True, metavar="username")
@click.argument('password', type=click.STRING, required=True, metavar="password")
@click.option('--file', '-f', type=click.Path(file_okay=True), default="users.json",
              help="File to persist the state.", required=True)
def authenticate(username, password, file):
    """Registers users."""
    is1 = ids.IdentityService()
    #print("file:", file)
    is1.load_to_json(file)
    ret = is1.authenticate(username, password)

    if ret:
        click.echo('User verified.')
    else:
        click.echo('User verification failed.')
