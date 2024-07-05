# django-unicorn-playground 🦄🛝

The `Unicorn Playground` provides a way to prototype and debug `Unicorn` components without creating a complete Django application.

## How to use

1. Create a new file called `app.py`
1. Add the following code to `app.py`

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "django-unicorn-playground"
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
        count += 1
    
    def subtract(self):
        count -= 1

UnicornPlayground.runserver(component=CounterView)
```

3. `python3 app.py`

## Acknowledgments

- [phoenix_playground](https://github.com/phoenix-playground/phoenix_playground)
