from unittest.mock import ANY, patch

from django_unicorn_playground import urls
from django_unicorn_playground.main import UnicornPlayground


@patch("django_unicorn_playground.main.django_conf_settings")
def test_configure(django_conf_settings):
    UnicornPlayground("tests/fake_components.py")

    components = {"fake_components": ANY}

    django_conf_settings.configure.assert_called_once_with(
        ALLOWED_HOSTS="*",
        ROOT_URLCONF=urls,
        SECRET_KEY=ANY,
        DEBUG=True,
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [ANY],
                "APP_DIRS": True,
                "OPTIONS": {"builtins": ["django_unicorn.templatetags.unicorn"]},
            }
        ],
        INSTALLED_APPS=("django.contrib.staticfiles", "django_unicorn", "django_unicorn_playground"),
        UNICORN={"COMPONENTS": components},
        STATIC_URL="static/",
    )
