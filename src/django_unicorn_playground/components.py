import importlib.machinery
import inspect
from pathlib import Path

from django_unicorn.components import UnicornView
from typeguard import typechecked


@typechecked
def get_component_classes(component_path: Path | str) -> list[type[UnicornView]]:
    """Create the component class based on the path of the component."""

    if not component_path:
        raise AssertionError("A component path must be passed in")

    if isinstance(component_path, str):
        component_path = Path(component_path)

    module = component_path.name.replace(component_path.suffix, "")

    # Inspect the passed-in component file and get all of the imported classes
    module = importlib.machinery.SourceFileLoader(module, str(component_path)).load_module()
    class_members = inspect.getmembers(module, inspect.isclass)

    # Get the UnicornView subclass in the component file
    unicorn_view_subclasses = [c[1] for c in class_members if issubclass(c[1], UnicornView) and c[1] is not UnicornView]

    if not unicorn_view_subclasses:
        raise AssertionError("No subclass of UnicornView found")

    return unicorn_view_subclasses
