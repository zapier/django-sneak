#!/usr/bin/env python
from __future__ import unicode_literals

import os
import sys

# add the `example` directory to `sys.path`, as it's where we need to import
# `configure_settings` from
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'example')))


if __name__ == '__main__':
    from django.conf import settings

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
