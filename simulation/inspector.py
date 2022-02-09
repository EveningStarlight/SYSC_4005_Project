from event import Event
from component import Component
import time

class Inspector:
    """docstring for Inspector."""


    def __init__(self, name, components, buffers, futureEvents, log):
        super(Inspector, self).__init__()
        self.name = name
        self.components = components
        self.buffers = buffers
        self.futureEvents = futureEvents
        self.log = log
        self._start_time = None

    def start(self):
        self.futureEvents.put(Event(0, self, self.getComponent))

    def getComponent(self, simulationTime):
        self.component = Component(self.components)
        self.futureEvents.put(Event(simulationTime+10, self, self.putComponent))
        self.log(str(self) + " grabbed " + str(self.component))

    def putComponent(self, simulationTime):
        buffer = min(self.buffers)
        if buffer.isFull():
            self.log(str(self) + " was blocked")
            self._start_time = time.perf_counter()
            while buffer.isFull():
                buffer = min(self.buffers)
            elapsed_time = time.perf_counter() - self._start_time
            self._start_time = None
            self.log(str(self) + " Blocked time: {elapsed_time:0.4f} seconds")
        buffer.putComponent(self.component)
        self.log(str(self) + " put component in " + str(buffer))
        self.getComponent(simulationTime)


    def __str__(self):
        return self.name
