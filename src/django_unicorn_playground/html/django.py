from typing import Any


def variable(var: Any) -> str:
    """Output a var as a DTL variable."""

    if var is None:
        return ""

    # TODO: Add filters?

    return "{{ " + str(var) + " }}"
