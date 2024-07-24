from pathlib import Path

from django.conf import settings


def pytest_configure():
    base_dir = Path(".")

    settings.configure(
        BASE_DIR=base_dir,
        SECRET_KEY="this-is-a-secret",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.template.context_processors.debug",
                        "django.template.context_processors.static",
                    ],
                    "builtins": [
                        "django_unicorn.templatetags.unicorn",
                    ],
                },
            }
        ],
        INSTALLED_APPS=[
            "django_unicorn",
            "tests",
        ],
        CACHES={
            "default": {
                "BACKEND": "django.core.cache.backends.dummy.DummyCache",
            }
        },
        UNICORN={},
        ROOT_URLCONF="tests.urls",
    )
