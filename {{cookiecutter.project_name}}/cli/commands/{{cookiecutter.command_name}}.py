#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""{{cookiecutter.command_name}}.py
"""
try:
    import ujson as json
except Exception as err:
    import json

from .base import Base

class {{cookiecutter.command_name.title()}}(Base):
    """{{cookiecutter.command_name.title()}} command
    Parameters
    ----------
    arg1 : lorem ipsum
    """
    def run(self):
        print('You called {{cookiecutter.command_name.title().run()')
        print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
