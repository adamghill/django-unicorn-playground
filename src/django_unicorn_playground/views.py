from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template.exceptions import TemplateDoesNotExist
from django_unicorn.components import UnicornView
from django_unicorn.utils import create_template
from typeguard import typechecked


@typechecked
def _get_default_index_template_html(components: dict[str, type[UnicornView]]) -> str:
    """Gets the default index template HTML with all components."""

    html = """{% extends "base.html" %}
{% block content %}
"""

    for component_name in components.keys():
        html += "{% unicorn '" + component_name + "' %}\n"

    html += """
{% endblock content %}"""

    return html


def index(request):
    """Default route for the developer server."""

    try:
        return render(request, "index.html")
    except TemplateDoesNotExist as e:
        if not hasattr(settings, "UNICORN"):
            raise AssertionError("Missing UNICORN setting") from e

        components = settings.UNICORN.get("COMPONENTS", {})

        if not components:
            raise AssertionError("No components could be found") from e

        index_template_html = _get_default_index_template_html(components)
        template = create_template(index_template_html, engine_name="django")
        content = template.render(context={"components": components})

        return HttpResponse(content)
