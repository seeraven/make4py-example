"""The answer module of make4py-example.

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


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------
# pylint: disable=too-few-public-methods
class Answers:
    """Answers for questions."""

    def __init__(self) -> None:
        """Constructor."""
        self._answers = {"why": "why not?", "where": "here", "what": "everything"}

    def get_answer(self, question: str) -> str:
        """Get the answer to a question.

        Args:
            question: The question.

        Return:
            Returns the answer.
        """
        for keyword, answer in self._answers.items():
            if keyword in question.lower():
                return answer
        return "no idea"


# -----------------------------------------------------------------------------
# EOF
# -----------------------------------------------------------------------------
