from event import Event
from component import Component
import random

class Inspector:
    """docstring for Inspector."""

    def __init__(self, name, components, buffers, futureEvents, log, times, seed):
        super(Inspector, self).__init__()
        self.name = name
        self.components = components
        self.buffers = buffers
        self.futureEvents = futureEvents
        self.log = log
        self.times = times
        self.seed = seed

    def start(self):
        self.futureEvents.put(Event(0, self, self.getComponent))

    def getComponent(self, simulationTime):
        self.component = Component(self.components)
        if(len(self.components)==1):
            self.futureEvents.put(Event(simulationTime+self.times.pop(0), self, self.putComponent))
        elif(len(self.components)==2):
            if(str(self.component)=="Component Type 2"):
                self.futureEvents.put(Event(simulationTime+self.times[0].pop(0), self, self.putComponent))
            elif(str(self.component)=="Component Type 3"):
                self.futureEvents.put(Event(simulationTime+self.times[1].pop(0), self, self.putComponent))
        else:
            raise ValueError('The configuration was done wrong')
        self.log(str(self) + " grabbed " + str(self.component))

    def putComponent(self, simulationTime):
        buffer = min(self.buffers)
        if buffer.isFull():
            #todo block and await
            self.log(str(self) + " was blocked")
            pass
        else:
            buffer.putComponent(self.component)
            self.log(str(self) + " put component in " + str(buffer))
            self.getComponent(simulationTime)


    def __str__(self):
        return self.name
