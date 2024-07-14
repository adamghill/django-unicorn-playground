from django.shortcuts import render
from django.template import Context, Template
from django.template.exceptions import TemplateDoesNotExist


def index(request):
    # Look for index.html, if it cannot be found use default html

    try:
        return render(request, "index.html")
    except TemplateDoesNotExist:
        template_code = """{% extends "base.html" %}
{% load unicorn %}

{% block content %}
{% unicorn 'counter' %}
{% endblock content %}
    """

        return Template(template_code).render(context=Context({}))
