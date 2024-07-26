# django-unicorn-playground 🦄🛝

The `Unicorn Playground` provides a way to prototype and debug [`Unicorn`](https://www.django-unicorn.com) components without creating a complete Django application. It can either be run as a standalone script or by installing the library.

## Standalone Script

The benefit of the standalone script is that dependencies are defined in the file and `pipx` handles creating the virtual environment when the script is running.

1. Install [`pipx`](https://pipx.pypa.io/latest/installation/)
2. Create a new file called `counter.py`
3. Add the following code to `counter.py`

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
    template_html = """<div>
    <div>
        Count: {{ count }}
    </div>

    <button unicorn:click="increment">+</button>
    <button unicorn:click="decrement">-</button>
</div>
"""

    count: int

    def increment(self):
        count += 1
    
    def decrement(self):
        count -= 1

if __name__ == "__main__":
    UnicornPlayground(__file__).runserver()
```

4. `pipx run counter.py`
5. Go to https://localhost:8000

## CLI

Another option is to install the `django-unicorn-playground` library. This provides a CLI that can be used to run components. This approach uses basically the same code, but doesn't require the script inline metadata or the call to `runserver` at the end -- the CLI takes care of running the development server directly. Those portions can be included, though, and will not prevent the CLI from being usable.

1. `pipx install django-unicorn-playground`
1. Create `counter.py` with the following code:

```python
from django_unicorn.components import UnicornView

class CounterView(UnicornView):
    template_html = """<div>
    <div>
        Count: {{ count }}
    </div>

    <button unicorn:click="increment">+</button>
    <button unicorn:click="decrement">-</button>
</div>
"""

    count: int

    def increment(self):
        count += 1
    
    def decrement(self):
        count -= 1
```

3. `unicorn counter.py`
4. Go to https://localhost:8000

## Example components

There are a few example components in the `examples` directory.

They can be run with something like `pipx run --no-cache examples/counter.py`.

## Template HTML

The component's HTML can be initialized in a few ways.

### UnicornView.template_file attribute

The HTML can be set with a class-level `template_html` field.

```python
from django_unicorn.components import UnicornView

class TestView(UnicornView):
    template_html = """<div>
    <div>
        Count: {{ count }}
    </div>

    <button unicorn:click="increment">+</button>
    <button unicorn:click="decrement">-</button>
</div>
"""

    ...
```

### UnicornView.template_file method

The HTML can be returns from a `template_html` instance method.

```python
from django_unicorn.components import UnicornView

class TestView(UnicornView):
    def template_html(self): 
        return """<div>
    <div>
        Count: {{ count }}
    </div>

    <button unicorn:click="increment">+</button>
    <button unicorn:click="decrement">-</button>
</div>
"""

    ...
```

### HTML file

Similar to a typical `django-unicorn` setup, the component HTML can be a separate template file. This is the fallback and will only be searched for if the `template_view` field or method is not defined on the component.

1. `cd` to the same directory as the component Python file you created
2. `mkdir -p templates/unicorn`
3. `touch {COMPONENT-NAME}.html`, e.g. for a component Python named `counter.py` create `counter.html`
4. Add the component HTML to the newly created file

## Using a Python HTML builder

Any Python library that generates normal HTML strings work great with `django-unicorn-playground`.

Some examples of libraries below:

### [haitch](https://pypi.org/project/haitch/)

 ```python
 import haitch
 from django_unicorn.components import UnicornView

 class TestComponent(UnicornView)
    def template_html(self):
        return haitch.div()(
            haitch.button("Increment +", **{"unicorn:click": "increment"}),
            haitch.button("Decrement -", **{"unicorn:click": "decrement"}),
            haitch.div("{{ count }}"),
        )
    
    ...
 ```

 ### [htpy](https://pypi.org/project/htpy/)

 ```python
 import htpy
 from django_unicorn.components import UnicornView

 class TestComponent(UnicornView)
    def template_html(self):
        return htpy.div()[
            htpy.button({"unicorn:click": "increment"})["Increment +"],
            htpy.button({"unicorn:click": "decrement"})["Decrement -"],
            htpy.div()["{{ count }}"],
        ]
    
    ...
 ```

 ### [dominate](https://pypi.org/project/dominate/)

 ```python
 from dominate import tags as dom
 from django_unicorn.components import UnicornView

 class TestComponent(UnicornView)
    def template_html(self):
        return dom.div(
            dom.button("Increment +", **unicorn.click(self.increment)),
            dom.button("Decrement -", **unicorn.click(self.decrement)),
            dom.div("{{ count }}"),
        )
    
    ...
 ```

## Unicorn HTML helpers

When using a Python HTML builder like the above, there are a few helper methods which make it a little cleaner to build Unicorn-specific HTML.

For example, if using `haitch` instead of doing this:

 ```python
 import haitch
 from django_unicorn.components import UnicornView

 class TestComponent(UnicornView)
    def template_html(self):
        return haitch.div()(
            haitch.button("Increment +", **{"unicorn:click": "increment"}),
            haitch.button("Decrement -", **{"unicorn:click": "decrement"}),
            haitch.div("{{ count }}"),
        )
    
    ...
 ```

Using helper methods:

 ```python
 import haitch
 from django_unicorn.components import UnicornView
 from django_unicorn_playground.html import django, unicorn

 class TestComponent(UnicornView)
    def template_html(self):
        return haitch.div()(
            haitch.button("Increment +", **unicorn.click(self.increment)),
            haitch.button("Decrement -", **unicorn.click(self.decrement)),
            haitch.div(django.variable("count")),
        )
    
    ...
 ```

## Local development

### Inline script metadata

Using the inline script metadata with `pipx` seems a little quirky and I could not get editable installs working reliably. I also tried `hatch run` which had it's own issues. Not sure if there are other approaches.

As far as I can tell, the best approach is to use an absolute file path like `"django_unicorn_playground @ file:///Users/adam/Source/adamghill/django-unicorn-playground/dist/django_unicorn_playground-0.1.0-py3-none-any.whl"` (note the triple forward-slash after "file:") as a dependency, and rebuilding and re-running the script without any caching like this: `poetry build && pipx run --no-cache examples/counter.py` any time you make a code change.

Note: you will need to update the component's dependency so it points to the path on your machine.

However, there is a `just` command to make re-building for local dev _slightly_ less painful.

1. [Install just](https://just.systems/man/en/chapter_4.html)
1. `just serve examples/counter.py`

### CLI

Working locally with the CLI is more straight-forward than the inline script metadata approach.

1. `poetry install`
1. `poetry run unicorn examples/counter.py`

## Acknowledgments

- [phoenix_playground](https://github.com/phoenix-playground/phoenix_playground)
