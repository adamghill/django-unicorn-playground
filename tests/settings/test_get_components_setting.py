from django_unicorn_playground.settings import _get_components_setting

from ..fake_components import FakeView


def test_get_components_setting():
    expected = {"tests.fake_components": FakeView}
    actual = _get_components_setting([FakeView])

    assert expected == actual
