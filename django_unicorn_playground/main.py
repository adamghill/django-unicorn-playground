from django_unicorn.components import UnicornView


class UnicornPlayground:
    def __init__(self, component_class: UnicornView, *args, **kwargs):
        self.component_class = component_class
        # TODO: Take kwargs and use them for Django settings ala `coltrane`

    def runserver(self, port: int = 8000):
        print("call Django runserver!", self.component_class, port)
