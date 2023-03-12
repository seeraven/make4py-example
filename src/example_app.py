#!/usr/bin/env python3
"""Example application.

Copyright:
    2023 by Clemens Rabe <clemens.rabe@clemensrabe.de>

    All rights reserved.

    This file is part of make4py-example (https://github.com/seeraven/make4py-example)
    and is released under the "BSD 3-Clause License". Please see the ``LICENSE`` file
    that is included as part of this package.
"""


# -----------------------------------------------------------------------------
# Module Import
# -----------------------------------------------------------------------------
import argparse
import sys

from app_mod.answers import Answers


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def get_parser() -> argparse.ArgumentParser:
    """Get the argument parser."""
    description = "An example app that you can ask questions."
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("question", help="The question to ask.", type=str)
    return parser


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    args = get_parser().parse_args()
    answers = Answers()
    print(answers.get_answer(args.question))
    sys.exit(0)


# -----------------------------------------------------------------------------
# EOF
# -----------------------------------------------------------------------------
