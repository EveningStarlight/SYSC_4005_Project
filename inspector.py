import event
import component

class Inspector:
    """docstring for Inspector."""

    def __init__(self, components, buffers, futureEvents):
        super(Inspector, self).__init__()
        self.components = components
        self.buffers = buffers
        self.futureEvents = futureEvents

    def start(self):
        self.futureEvents.put(event.Event(0, self, self.getComponent))

    def getComponent(self, simulationTime):
        self.component = component.Component(self.components)
        self.futureEvents.put(event.Event(simulationTime+10, self, self.putComponent))
        print(str(self) + " grabbed " + str(self.component))

    def putComponent(self, simulationTime):
        buffer = min(self.buffers)
        if buffer.isFull():
            #todo block and await
            pass
        else:
            buffer.putComponent(self.self.component)
            self.getComponent(simulationTime)

    def __str__(self):
        return "Inspector " + str(self.components)
