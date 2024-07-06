# django-unicorn-playground 🦄🛝

The `Unicorn Playground` provides a way to prototype and debug `Unicorn` components without creating a complete Django application.

## Standalone Script

1. Install [`pipx`](https://pipx.pypa.io/latest/installation/)
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

UnicornPlayground(CounterView).runserver()
```

3. `pipx run app.py`
4. Go to https://localhost:8000

## Installable CLI

Installing `django-unicorn-playground` provides a CLI that can be used to run components.

1. `pipx install django-unicorn-playground`
1. Create `counter.py` with the following code:

```python
from django_unicorn.components import UnicornView

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
```

3. `unicorn counter.py`
4. Go to https://localhost:8000

## Example components

There are a few example components in the `examples` directory.

They can be run with something like `pipx run --no-cache examples/counter.py`.

## Local development

### Inline script metadata

Using the inline script metadata with `pipx` seems a little quirky and I could not get editable installs working reliably. I also tried `hatch run` which had it's own issues. Not sure if there are other approaches.

As far as I can tell, the best approach is to use an absolute file path like `"django_unicorn_playground @ file:///Users/adam/Source/adamghill/django-unicorn-playground/dist/django_unicorn_playground-0.1.0-py3-none-any.whl"` as a dependency, and rebuilding and re-running the script without any caching like this: `poetry build && pipx run --no-cache examples/counter.py` any time you make a code change.

You will need to update the component's dependency so it points to the path on your machine.

However, I have created a `just` command to make re-building for local dev _slightly_ less painful.

1. [Install just](https://just.systems/man/en/chapter_4.html)
1. `just serve examples/counter.py`

### CLI

Working locally with the CLI isn't quite as complicated.

1. `poetry install`
1. `poetry run unicorn examples/counter.py`

## Acknowledgments

- [phoenix_playground](https://github.com/phoenix-playground/phoenix_playground)
