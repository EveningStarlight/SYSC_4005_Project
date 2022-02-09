from event import Event
from component import Component

class Inspector:
    """docstring for Inspector."""


    def __init__(self, name, components, buffers, futureEvents, log):
        super(Inspector, self).__init__()
        self.name = name
        self.components = components
        self.buffers = buffers
        self.futureEvents = futureEvents
        self.log = log
        self.blockedTime = 0
        self.blockTimeStart = 0

    def start(self):
        self.futureEvents.put(Event(0, self, self.getComponent))
        self.log(str(self) + " Started ")

    def getComponent(self, simulationTime):
        self.component = Component(self.components)
        self.futureEvents.put(Event(simulationTime+10, self, self.putComponent))
        self.log(str(self) + " grabbed " + str(self.component))

    def putComponent(self, simulationTime):
        buffer = min(self.buffers)
        if buffer.isFull() and self.blockTimeStart == 0:
            self.blockTimeStart = simulationTime
            self.log(str(self) + " was blocked")
            self.futureEvents.put(Event(simulationTime+10, self, self.putComponent))
        elif buffer.isFull():
            self.futureEvents.put(Event(simulationTime+10, self, self.putComponent))
        else:
            self.blockedTime += self.blockTimeStart
            self.blockTimeStart = 0
            buffer.putComponent(self.component)
            self.log(str(self) + " put component in " + str(buffer))
            self.getComponent(simulationTime)


    def __str__(self):
        return self.name
