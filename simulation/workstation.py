from event import Event
from buffer import Buffer
import random

class Workstation:
    """docstring for Workstation."""

    def __init__(self, name, buffers, product, futureEvents, log, times, seed):
        super(Workstation, self).__init__()
        self.name = name
        self.buffers = buffers
        self.product = product
        self.futureEvents = futureEvents
        self.log = log
        self.productsMade = 0
        self.times = times
        self.seed = seed

    def getComponents(self):
        random.Random(self.seed).shuffle(self.times)
        if all(map(Buffer.hasComponent, self.buffers)):
            self.components = list(map(Buffer.get, self.buffers))
            self.futureEvents.put(Event(0+self.times[0], self, finishProduct))
            self.log(str(self) + " grabbed from " + str(self.buffers))
        else:
            #todo implement blocking
            self.log(str(self) + " was blocked")
            pass

    def finishProduct(self):
        self.productsMade += 1
        self.components = []
        self.log(str(self) + " finished a product")

        self.getComponents()

    def __str__(self):
        return self.name
