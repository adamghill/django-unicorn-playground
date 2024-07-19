from typing import Any


def variable(var: Any) -> str:
    return "{{ " + str(var) + " }}"
