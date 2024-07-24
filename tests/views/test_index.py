import pytest
from django_unicorn.errors import MissingComponentElementError

from django_unicorn_playground.views import index
from tests.fake_components import FakeView


def test_index(rf, settings):
    settings.UNICORN = {"COMPONENTS": {"fake-view": FakeView}}

    request = rf.get("/")

    response = index(request)
    assert response.status_code == 200

    settings.UNICORN = {}


def test_index_invalid_template(rf, settings):
    settings.UNICORN = {"COMPONENTS": {"bad-fake-view": FakeView}}

    request = rf.get("/")

    with pytest.raises(MissingComponentElementError) as e:
        index(request)

    assert (
        e.exconly() == "django_unicorn.errors.MissingComponentElementError: No root element for the component was found"
    )

    settings.UNICORN = {}


def test_index_missing_unicorn_setting(rf, settings):
    del settings.UNICORN

    request = rf.get("/")

    with pytest.raises(AssertionError) as e:
        index(request)

    assert e.exconly() == "AssertionError: Missing UNICORN setting"

    settings.UNICORN = {}


def test_index_missing_unicorn_components(rf, settings):
    settings.UNICORN = {"COMPONENTS": {}}

    request = rf.get("/")

    with pytest.raises(AssertionError) as e:
        index(request)

    assert e.exconly() == "AssertionError: No components could be found"

    settings.UNICORN = {}
