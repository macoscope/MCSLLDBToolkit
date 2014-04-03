#!/usr/bin/env python
# encoding: utf-8

from mcslldb_helpers import lldb_command


@lldb_command
def uppercase(debugger, *args):
    return '\n'.join(x.upper() for x in args)
