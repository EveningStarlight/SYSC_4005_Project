from event import Event
from buffer import Buffer

class Workstation:
    """docstring for Workstation."""

    def __init__(self, name, buffers, product, futureEvents, log):
        super(Workstation, self).__init__()
        self.name = name
        self.buffers = buffers
        self.product = product
        self.futureEvents = futureEvents
        self.log = log
        self.productsMade = 0
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
            self.futureEvents.put(Event(simulationTime+40, self, self.finishProduct))
            self.log(str(self) + " grabbed from " + str(self.buffers))
        elif self.blockTimeStart == 0:
            self.blockTimeStart = simulationTime
            self.log(str(self) + " was blocked")
            self.futureEvents.put(Event(simulationTime+10, self, self.getComponents))
        else:
            self.futureEvents.put(Event(simulationTime+10, self, self.getComponents))

    def finishProduct(self, simulationTime):
        self.productsMade += 1
        self.components = []
        self.log(str(self) + " finished product #" + str(self.productsMade))

        self.futureEvents.put(Event(simulationTime+10, self, self.getComponents))

    def __str__(self):
        return self.name

    def end(self, simulationTime):
        if self.blockTimeStart != 0:
                self.blockedTime += (simulationTime - self.blockTimeStart)
                self.blockTimeStart = 0
        self.log(str(self) + " Total Blocked Time: " + str(self.blockedTime))
