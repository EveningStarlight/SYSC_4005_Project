class Inspector(object):
    """docstring for Inspector."""

    def __init__(self, components, buffers, processingTime):
        super(Inspector, self).__init__()
        self.components = components
        self.buffers = buffers
        self.processingTime = processingTime

class Buffer(object):
    """docstring for Buffer."""

    def __init__(self, component, product):
        super(Buffer, self).__init__()
        self.component = component
        self.product = product
        self.buffer = queue.Queue(maxsize=2)

    def isFull(self):
        self.buffer.full()

    def addComponent(self, component):
        self.buffer.put(component)


class Workstation(object):
    """docstring for Workstation."""

    def __init__(self, buffers, product, processingTime):
        super(Workstation, self).__init__()
        self.buffers = buffers
        self.product = product
        self.processingTime = processingTime


class Component(object):
    """docstring for Component."""

    def __init__(self, componentTypes):
        super(Component, self).__init__()
        self.type = random.choice(componentTypes)


def main():
    workstation1Buffer = Buffer(component=1, product=1)
    workstation1 = Workstation(buffers=[workstation1Buffer])

    workstation2Buffer_C1 = Buffer(component=1, product=2)
    workstation2Buffer_C2 = Buffer(component=2, product=2)
    workstation2 = Workstation(buffers = [workstation2Buffer_C1,workstation2Buffer_C2])

    workstation3Buffer_C1 = Buffer(component=1, product=3)
    workstation3Buffer_C3 = Buffer(component=3, product=3)
    workstation3 = Workstation(buffers=[workstation3Buffer_C1, workstation3Buffer_C3])

    inspector1 = Inspector(components=[1], buffers=[workstation1Buffer, workstation2Buffer_C1, workstation3Buffer_C1])
    inspector2 = Inspector(components=[2,3], buffers=[workstation2Buffer_C2, workstation3Buffer_C3])
