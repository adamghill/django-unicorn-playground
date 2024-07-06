from django_unicorn.components import UnicornView


class UnicornPlayground:
    def runserver(self, component: UnicornView):
        print("call Django runserver")
