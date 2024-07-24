from django_unicorn_playground.views import _get_default_index_template_html
from tests.fake_components import FakeView


def test_get_default_index_template_html():
    expected = """{% extends "base.html" %}
{% block content %}

{% endblock content %}"""
    actual = _get_default_index_template_html(components={})

    assert expected == actual


def test_get_default_index_template_html_components():
    expected = """{% extends "base.html" %}
{% block content %}
{% unicorn 'fake-component' %}

{% endblock content %}"""

    components = {"fake-component": FakeView}
    actual = _get_default_index_template_html(components=components)

    assert expected == actual
