#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""{{cookiecutter.project_name}} - generate a python CLI app

Usage:
    {{cookiecutter.project_name}} {{cookiecutter.command_name}}
    {{cookiecutter.project_name}} -h | --help
    {{cookiecutter.project_name}} --version

Options:
    -h --help                         Show this screen.
    --version                         Show version.

Examples:
    {{cookiecutter.project_name}} {{cookiecutter.command_name}}

Help:
    For help using this tool TODO
"""

from inspect import getmembers, isclass
from docopt import docopt

VERSION  = '1.0.0'

def main():
    """Main CLI entrypoint."""
    import cli.commands as commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for k, v in options.items():
        if hasattr(commands, k):
            module = getattr(commands, k)
            commands = getmembers(module, isclass)
            command = [command[1] for command in commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
