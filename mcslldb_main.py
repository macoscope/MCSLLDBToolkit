#!/usr/bin/env python
# encoding: utf-8

from mcslldb_helpers import DummyDebugger, register_commands


def __lldb_init_module(debugger, internal_dict):
    import mcslldb_commands
    assert mcslldb_commands  # silence pyflakes

    register_commands(debugger)


if __name__ == '__main__':
    __lldb_init_module(DummyDebugger(), {})
