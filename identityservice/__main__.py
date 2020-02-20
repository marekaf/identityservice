#!/usr/bin/env python3
"""
A simple identity service which keeps its state in the memory
and is able to save/load its state to/from a file and a Command
Line Interface (CLI) that can be used to register a new user
and authenticate an existing user.
"""

from identityservice import cli

if __name__ == '__main__':
    cli.cli()
