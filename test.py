#!/usr/bin/env python
# encoding: utf-8
import cm
from cm.options.path import base
from cm.options.db import port, name

port.type = int
port.default = 10
port.help = "Lolwat"
base.help = "Base path"

if __name__ == '__main__':
    cm.parse_command_line()