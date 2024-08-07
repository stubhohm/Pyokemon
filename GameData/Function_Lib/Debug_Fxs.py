from ..GlobalVars import debug

class Debugging():
    def __init__(self):
        self.debug = debug
    
    def print(self, value):
        if self.debug:
            print(value)

    
