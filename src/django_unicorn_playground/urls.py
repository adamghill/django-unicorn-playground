from django.urls import include, path

from django_unicorn_playground.views import index

urlpatterns = [
    path("", index),
    path("unicorn/", include("django_unicorn.urls")),
]
