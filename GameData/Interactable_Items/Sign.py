from ..Class_lib.Interactable import Interactable
from ..Class_lib.UI import ui

class Sign(Interactable):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.sign_text = None

    def set_display_text(self, text: str):
        self.sign_text = text

    def define_sign(self, display_text:str, coordinate: tuple):
        super().set_coordinate(coordinate)
        self.set_display_text(display_text)

    def interact(self):
        super().interact()
        if not self.sign_text:
            print('No attributed text')
        super().print_to_terminal(self.sign_text)
