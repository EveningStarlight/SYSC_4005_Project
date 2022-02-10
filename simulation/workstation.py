from event import Event
from buffer import Buffer
import random

class Workstation:
    """docstring for Workstation."""

    def __init__(self, name, buffers, product, futureEvents, blockedQueue, log, times, seed):
        super(Workstation, self).__init__()
        self.name = name
        self.buffers = buffers
        self.product = product
        self.futureEvents = futureEvents
        self.blockedQueue = blockedQueue
        self.log = log
        self.productsMade = 0
        self.times = times
        self.seed = seed
        self.components = []
        self.blockedTime = 0
        self.blockTimeStart = 0

    def start(self):
        self.futureEvents.put(Event(20, self, self.getComponents))
        self.log(str(self) + " Started ")

    def getComponents(self, simulationTime):
        if all(map(Buffer.hasComponent, self.buffers)):
            if self.blockTimeStart != 0:
                self.blockedTime += (simulationTime - self.blockTimeStart)
                self.blockTimeStart = 0
            self.components = list(map(Buffer.get, self.buffers))
            self.futureEvents.put(Event(simulationTime+self.times.pop(0), self, self.finishProduct))
            self.log(str(self) + " grabbed from " + str(self.buffers))
        elif self.blockTimeStart == 0:
            self.blockTimeStart = simulationTime
            self.log(str(self) + " was blocked", colour="yellow")
            self.blockedQueue.put(Event(simulationTime, self, self.getComponents))
        else:
            self.blockedQueue.put(Event(simulationTime, self, self.getComponents))

    def finishProduct(self, simulationTime):
        self.productsMade += 1
        self.components = []
        self.log(str(self) + " finished product #" + str(self.productsMade))

        self.getComponents(simulationTime)

    def __str__(self):
        return self.name

    def end(self, simulationTime):
        if self.blockTimeStart != 0:
                self.blockedTime += (simulationTime - self.blockTimeStart)
                self.blockTimeStart = 0
