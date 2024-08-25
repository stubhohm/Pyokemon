from ..Class_lib.Interactable import Interactable

class HealingStation(Interactable):
    def __init__(self, name) -> None:
        super().__init__(name)

    def interact(self):
        print('healing your pokemon via station')
        super().interact()

