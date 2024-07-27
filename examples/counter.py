# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "django_unicorn_playground"
# ]
# ///

from django_unicorn.components import UnicornView


class CounterView(UnicornView):
    template_html = """<div>
    <button unicorn:click="increment">Increment +</button>
    <button unicorn:click="decrement">Decrement -</button>

    <div>
    {{ count }}
    </div>
</div>
"""

    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


if __name__ == "__main__":
    from django_unicorn_playground import UnicornPlayground

    UnicornPlayground(__file__).runserver()
