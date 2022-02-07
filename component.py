import random

class Component:
    """docstring for Component."""

    def __init__(self, componentTypes):
        super(Component, self).__init__()
        self.type = random.choice(componentTypes)

    def __str__(self):
        return "Component Type " + str(self.type)
