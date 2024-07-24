from pathlib import Path

import pytest
import typeguard
from django_unicorn.components import UnicornView

from django_unicorn_playground.components import get_component_classes


def test_get_component_classes_str():
    actual = get_component_classes("tests/fake_components.py")

    assert len(actual) == 1

    component_class = actual[0]
    assert issubclass(component_class, UnicornView)

    assert component_class.__name__ == "FakeView"


def test_get_component_classes_path():
    actual = get_component_classes(Path("tests/fake_components.py"))

    assert len(actual) == 1

    component_class = actual[0]
    assert issubclass(component_class, UnicornView)

    assert component_class.__name__ == "FakeView"


def test_get_component_classes_none():
    with pytest.raises(typeguard.TypeCheckError):
        get_component_classes(None)


def test_get_component_classes_empty_str():
    with pytest.raises(AssertionError) as e:
        get_component_classes("")

    assert e.exconly() == "AssertionError: A component path must be passed in"


def test_get_component_classes_no_unicorn_views():
    with pytest.raises(AssertionError) as e:
        get_component_classes(__file__)

    assert e.exconly() == "AssertionError: No subclass of UnicornView found"
