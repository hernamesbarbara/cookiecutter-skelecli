#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""cmd1.py
"""
try:
    import ujson as json
except Exception as err:
    import json

from .base import Base

class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print('Hello, world!')
        print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
