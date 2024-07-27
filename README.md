# django-unicorn-playground 🦄🛝

The `Unicorn Playground` provides a way to prototype and debug [`Unicorn`](https://www.django-unicorn.com) components without creating a complete Django application. It can either be run as a standalone script or by installing the library.

https://github.com/user-attachments/assets/43533156-deba-4cc1-811b-045115054c73

## Standalone

A python script runner, like `pipx`, can create the virtual environment and install dependencies automatically. [Inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/) provides the required dependency information for `pipx`.

### Create an example component

1. Install [`pipx`](https://pipx.pypa.io/latest/installation/)
2. Create a new file called `counter.py` with the following code:

```python
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "django-unicorn-playground"
# ]
# ///

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

if __name__ == "__main__":
    from django_unicorn_playground import UnicornPlayground

    UnicornPlayground(__file__).runserver()
```

3. `pipx run counter.py`
4. Go to https://localhost:8000

### Python script runners

`pipx` is officially supported, but some other script runners should also work.

#### [pip-run](https://github.com/jaraco/pip-run)

`pip-run counter.py`

#### [fades](https://github.com/PyAr/fades)

`fades -d django-unicorn-playground counter.py`

## CLI

The `django-unicorn-playground` library can also be installed and provides a command-line interface. This approach doesn't require the script inline metadata or the check for `__name__` -- the CLI takes care of running the development server directly.

### Create an example component

1. `pipx install django-unicorn-playground`
2. Create `counter.py` with the following code:

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

### Arguments

#### component

The path to the component. Required.

#### --port

Port for the developer webserver. Required to be an integer. Defaults to 8000.

#### --template_dir

Directory for templates. Required to be a string path.

#### --version

Shows the current version.

#### --help

Show the available CLI options.

## Example components

There are a few example components in the `examples` directory. They can be run with something like `pipx run --no-cache examples/counter.py`.

## Template HTML

### UnicornView.template_html attribute

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

### UnicornView.template_html(self)

The HTML can be returned from a `template_html` instance method.

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

Similar to a typical `django-unicorn` setup, the component HTML can be in a separate template file. This file will be looked for if `template_html` is not defined on the component.

1. `cd` to the same directory as the component Python file you created
2. `mkdir -p templates/unicorn`
3. `touch {COMPONENT-NAME}.html`, e.g. for a component Python named `counter.py` create `counter.html`
4. Add the component HTML to the newly created file

### Template directory

By default `django-unicorn-playground` will look in the `templates/unicorn` folder for templates. The template location can be changed by passing in a `template_dir` kwarg into the `UnicornPlayground()` constructor or using a `--template_dir` argument to the CLI.

### index.html

The root URL dynamically creates `index.html` which creates HTML for the component. It looks something like the following.

```html
{% extends "base.html" %}
{% block content %}
{% unicorn 'COMPONENT-NAME' %}
{% endblock content %}
```

It can be overridden by creating a custom `index.html` in the template directory.

### base.html

By default, `index.html` extends [`base.html`](https://github.com/adamghill/django-unicorn-playground/blob/main/src/django_unicorn_playground/templates/base.html). It looks something like the following.

```html
<html>

<head>
  {% unicorn_scripts %}
</head>

{% block content %}
{% endblock content %}

</html>
```

It can be overridden by creating a custom `base.html` in the template directory.

## Using a Python HTML builder

Any Python library that generates HTML strings works great with `django-unicorn-playground`.

### [haitch](https://pypi.org/project/haitch/)

 ```python
 from django_unicorn.components import UnicornView
 import haitch

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
 from django_unicorn.components import UnicornView
 import htpy

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
 from django_unicorn.components import UnicornView
 from dominate import tags as dom

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

When using an HTML builder, `django-unicorn-playground` provides a few helper methods which make it a little cleaner to create `Unicorn`-specific HTML.

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

This is how it would work with the helper methods:

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

### Standalone

Using the inline script metadata with `pipx` seems a little quirky and I could not get editable installs working reliably. I also tried `hatch run` which had its own issues. Not sure if there are other (read: better) approaches.

As far as I can tell, the best approach is to use an absolute file path like `"django_unicorn_playground @ file:///Users/adam/Source/adamghill/django-unicorn-playground/dist/django_unicorn_playground-0.1.0-py3-none-any.whl"` (note the triple forward-slash after "file:") as a dependency, and rebuilding and re-running the script without any caching like this: `poetry build && pipx run --no-cache examples/counter.py` any time you make a code change.

Note: you will need to update the component's dependency so it points to the path and version on your machine.

There is a `just` command to make testing a standalone script _slightly_ less painful during local development.

1. [Install just](https://just.systems/man/en/chapter_4.html)
1. `just serve {COMPONENT-FILE-PATH}`, e.g. `just serve examples/counter.py`

### CLI

1. `poetry install`
1. `poetry run unicorn {COMPONENT-FILE-PATH}`, e.g. `poetry run unicorn examples/counter.py`

## Acknowledgments

- [phoenix_playground](https://github.com/phoenix-playground/phoenix_playground)
