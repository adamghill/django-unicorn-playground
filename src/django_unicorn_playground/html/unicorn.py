from collections.abc import Callable
from typing import Literal

from typeguard import typechecked

EVENT_LITERALS = Literal[
    "DOMContentLoaded",
    "afterprint",
    "beforeprint",
    "beforematch",
    "beforetoggle",
    "beforeunload",
    "blur",
    "cancel",
    "change",
    "click",
    "close",
    "connect",
    "contextlost",
    "contextrestored",
    "currententrychange",
    "dispose",
    "error",
    "focus",
    "formdata",
    "hashchange",
    "input",
    "invalid",
    "languagechange",
    "load",
    "message",
    "messageerror",
    "navigate",
    "navigateerror",
    "navigatesuccess",
    "offline",
    "online",
    "open",
    "pageswap",
    "pagehide",
    "pagereveal",
    "pageshow",
    "pointercancel",
    "popstate",
    "readystatechange",
    "rejectionhandled",
    "reset",
    "select",
    "storage",
    "submit",
    "toggle",
    "unhandledrejection",
    "unload",
    "visibilitychange",
]


@typechecked
def click(method: Callable | str) -> dict:
    return action("click", method)


@typechecked
def submit(method: Callable | str) -> dict:
    return action("submit", method)


@typechecked
def blur(method: Callable | str) -> dict:
    return action("submit", method)


@typechecked
def change(method: Callable | str) -> dict:
    return action("change", method)


@typechecked
def focus(method: Callable | str) -> dict:
    return action("focus", method)


@typechecked
def input(method: Callable | str) -> dict:  # noqa: A001
    return action("input", method)


@typechecked
def action(event: EVENT_LITERALS, method: Callable | str) -> dict:
    if callable(method):
        method = method.__name__

    return {f"unicorn:{event}": method}
