import event

import queue

class Buffer:
    """docstring for Buffer."""

    def __init__(self, component, product, futureEvents, initTime):
        super(Buffer, self).__init__()
        self.name = "Buffer " + str(product) + "-" + str(component)
        self.component = component
        self.product = product
        self.buffer = queue.Queue(maxsize=2)
        self.futureEvents = futureEvents
        self.averageComponents = 0
        self.previousTime = 0
        self.initTime = initTime

    def isFull(self):
        return self.buffer.full()

    def isEmpty(self):
        return self.buffer.empty()

    def putComponent(self, component, time):
        self.updateAverageComponents(time)
        self.buffer.put(component)

    def getComponent(self, time):
        self.updateAverageComponents(time)
        return self.buffer.get()

    def updateAverageComponents(self, time):
        if(time>self.initTime):
            self.averageComponents += self.buffer.qsize() * (time-self.previousTime)
        self.previousTime = time

    def end(self, time):
        self.updateAverageComponents(time)

    def __lt__(self, other):
        if self.buffer.qsize() < other.buffer.qsize():
            return self.buffer.qsize() < other.buffer.qsize()
        else:
            return self.product < other.product

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def hasComponent(buffer):
        return not buffer.isEmpty()

    def get(buffer, time):
        return buffer.getComponent(time)
