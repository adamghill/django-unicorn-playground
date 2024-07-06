# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "django_unicorn_playground @ file:///Users/adam/Source/adamghill/django-unicorn-playground/dist/django_unicorn_playground-0.1.0-py3-none-any.whl"
# ]
# ///

from django_unicorn.components import UnicornView

from django_unicorn_playground import UnicornPlayground


class CounterView(UnicornView):
    count: int

    template_html = """
<span>{{ count }}</span>
<button unicorn:click="add">+</button>
<button unicorn:click="subtract">-</button>
"""

    def add(self):
        self.count += 1

    def subtract(self):
        self.count -= 1


#  TODO: Should checking for __main__ be required? It feels ugly, but it is pretty standard Python.
# if __name__ == "__main__":
#     UnicornPlayground(CounterView).runserver()

UnicornPlayground(CounterView).runserver()
