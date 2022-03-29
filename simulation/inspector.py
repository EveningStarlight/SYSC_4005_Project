from event import Event
from component import Component
import random

class Inspector:
    """docstring for Inspector."""

    def __init__(self, name, components, buffers, futureEvents, blockedQueue, log, times, seed, initTime):
        super(Inspector, self).__init__()
        self.name = name
        self.components = components
        self.buffers = buffers
        self.futureEvents = futureEvents
        self.blockedQueue = blockedQueue
        self.log = log
        self.times = times
        self.seed = seed
        self.blockedTime = 0
        self.blockTimeStart = 0
        self.initTime = initTime

    def start(self):
        self.futureEvents.put(Event(0, self, self.getComponent))
        self.log(str(self) + " Started ")

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
        if buffer.isFull() and self.blockTimeStart == 0:
            if(simulationTime>initTime):
                self.blockTimeStart = simulationTime
                
            self.log(str(self) + " was blocked", colour="yellow")
            self.blockedQueue.put(Event(simulationTime, self, self.putComponent))
        elif buffer.isFull():
            self.blockedQueue.put(Event(simulationTime, self, self.putComponent))
        else:
            if self.blockTimeStart != 0:
                self.blockedTime += (simulationTime - self.blockTimeStart)
                self.blockTimeStart = 0
            buffer.putComponent(self.component, simulationTime)
            self.log(str(self) + " put component in " + str(buffer))
            self.getComponent(simulationTime)


    def __str__(self):
        return self.name

    def end(self, simulationTime):
        if self.blockTimeStart != 0:
                self.blockedTime += (simulationTime - self.initTime - self.blockTimeStart)
                self.blockTimeStart = 0
