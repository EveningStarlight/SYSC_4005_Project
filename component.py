class Component(object):
    """docstring for Component."""

    def __init__(self, componentTypes):
        super(Component, self).__init__()
        self.type = random.choice(componentTypes)
