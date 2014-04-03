#!/usr/bin/env python
# encoding: utf-8

from functools import wraps
import shlex
import sys


LLDB_COMMANDS = []


class DummyDebugger(object):

    def HandleCommand(self, s):
        print s


def lldb_command(function):
    r"""
    Decorate command functions.

    Example:

        @lldb_command
        def uppercase(debugger, *args):
            return '\n'.join(x.upper() for x in args)

    Usage:

        (lldb) uppercase foo bar baz
        FOO
        BAR
        BAZ

    """

    @wraps(function)
    def wrapper(debugger, argument_string, result_file, internal_dict):
        args = shlex.split(argument_string)
        result = function(debugger, *args)

        if result:
            result_file.write(result)
            result_file.write('\n')

    LLDB_COMMANDS.append(wrapper)

    return wrapper


def register_commands(debugger):
    imported_module_names = set()

    for function in LLDB_COMMANDS:
        function_name = function.__name__
        module_name = function.__module__

        if module_name not in imported_module_names:
            module_path = sys.modules[module_name].__file__.rstrip('c')
            debugger.HandleCommand('command script import %s' % module_path)
            imported_module_names.add(module_name)

        debugger.HandleCommand('command script add -f %s.%s %s' % \
            (module_name, function_name, function_name))
