from event import Event
from buffer import Buffer

class Workstation:
    """docstring for Workstation."""

    def __init__(self, buffers, futureEvents):
        super(Workstation, self).__init__()
        self.buffers = buffers
        self.futureEvents = futureEvents
        self.productsMade = 0

    def getComponents(self):
        if all(map(Buffer.hasComponent, self.buffers)):
            self.components = list(map(Buffer.get, self.buffers))
            self.futureEvents.put(Event(0+10, self, finishProduct))
        else:
            #todo implement blocking
            pass

    def finishProduct(self):
        self.productsMade += 1
        self.components = []

        self.getComponents()
