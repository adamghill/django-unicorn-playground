# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "django_unicorn_playground @ file:///Users/adam/Source/adamghill/django-unicorn-playground/dist/django_unicorn_playground-0.1.0-py3-none-any.whl"
# ]
# ///

from django_unicorn.components import UnicornView

from django_unicorn_playground import UnicornPlayground


class CounterView(UnicornView):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


if __name__ == "__main__":
    UnicornPlayground(__file__).runserver()
