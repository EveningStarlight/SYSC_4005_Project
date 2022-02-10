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
        return self.buffer.full()

    def isEmpty(self):
        return self.buffer.empty()

    def putComponent(self, component):
        self.buffer.put(component)

    def getComponent(self):
        return self.buffer.get()

    def __lt__(self, other):
        if self.buffer.qsize() < other.buffer.qsize():
            return self.buffer.qsize() < other.buffer.qsize()
        else:
            return self.product < other.product

    def __str__(self):
        return "Buffer " + str(self.product) + "-" + str(self.component)

    def __repr__(self):
        return str(self)

    def hasComponent(buffer):
        return not buffer.isEmpty()

    def get(buffer):
        return buffer.getComponent()
