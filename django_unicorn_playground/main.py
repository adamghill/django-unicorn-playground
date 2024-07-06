from django_unicorn.components import UnicornView


class UnicornPlayground:
    def runserver(self, component_class: UnicornView):
        print("call Django runserver!", component_class)
