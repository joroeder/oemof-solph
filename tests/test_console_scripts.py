"""
This file is part of project oemof (github.com/oemof/oemof). It's copyrighted by
the contributors recorded in the version control history of the file, available
from its original location oemof/tests/test_processing.py

SPDX-License-Identifier: GPL-3.0-or-later
"""

import oemof.tools.console_scripts as console_scripts

def check_console_scripts():
    console_scripts.check_oemof_installation()

if __name__ == "__main__":
    check_console_scripts()