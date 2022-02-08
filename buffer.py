import event

import queue

class Buffer:
    """docstring for Buffer."""

    def __init__(self, component, product, futureEvents):
        super(Buffer, self).__init__()
        self.component = component
        self.product = product
        self.buffer = queue.Queue(maxsize=2)
        self.futureEvents = futureEvents

    def isFull(self):
        self.buffer.full()

    def isEmpty(self):
        self.buffer.empty()

    def addComponent(self, component):
        self.buffer.put(component)

    def removeComponent(self):
        return self.buffer.get()

    def __lt__(self, other):
        if self.buffer.size < other.buffer.size:
            return self.buffer.size < other.buffer.size
        else:
            return self.product < other.product

    def hasComponent(buffer):
        return not buffer.isEmpty()

    def get(buffer):
        return buffer.get()
