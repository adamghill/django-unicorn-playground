import ast
import importlib.machinery
import inspect
from pathlib import Path

from django_unicorn.components import UnicornView


def get_component_class_ast(component_path: Path) -> type:
    """Downside of this is that it has to run exec/eval which are "unsafe"."""

    parsed_ast = ast.parse(component_path.read_text())

    class_defs = [node for node in ast.walk(parsed_ast) if isinstance(node, (ast.ClassDef))]

    for class_def in class_defs:
        class_name = class_def.name
        class_code = ast.unparse(class_def)

        exec(class_code)  # noqa: S102
        cls = eval(class_name)  # noqa: S307

        if issubclass(cls, UnicornView):
            return cls

    raise AssertionError("No subclass of UnicornView found")


def get_component_class_import(component_path: Path) -> type:
    """Create the component class based on the path of the component."""

    module = component_path.name.replace(component_path.suffix, "")

    # Inspect the passed-in component file and get all of the imported classes
    module = importlib.machinery.SourceFileLoader(module, str(component_path)).load_module()
    class_members = inspect.getmembers(module, inspect.isclass)

    # Get the UnicornView subclass in the component file
    unicorn_view_subclasses = [c[1] for c in class_members if issubclass(c[1], UnicornView) and c[1] is not UnicornView]

    assert unicorn_view_subclasses, "No subclass of UnicornView found"
    unicorn_view_subclass = unicorn_view_subclasses[0]

    return unicorn_view_subclass
