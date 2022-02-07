import event

class Buffer(object):
    """docstring for Buffer."""

    def __init__(self, component, product, futureEvents):
        super(Buffer, self).__init__()
        self.component = component
        self.product = product
        self.buffer = queue.Queue(maxsize=2)
        self.futureEvents = futureEvents

    def isFull(self):
        self.buffer.full()

    def addComponent(self, component):
        self.buffer.put(component)
