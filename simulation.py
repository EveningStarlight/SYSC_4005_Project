import event
import inspector
import buffer
import workstation

import queue

class Simulation:
    """docstring for Component."""

    def __init__(self, simulationTime, seed):
        super(Simulation, self).__init__()

        self.seed = seed

        self.futureEvents = queue.PriorityQueue()
        self.futureEvents.put(event.Event(simulationTime, self, "end"))

        self.workstation1Buffer = buffer.Buffer(component=1, product=1, futureEvents=self.futureEvents)
        self.workstation1 = workstation.Workstation(buffers=[self.workstation1Buffer], futureEvents=self.futureEvents)

        self.workstation2Buffer_C1 = buffer.Buffer(component=1, product=2, futureEvents=self.futureEvents)
        self.workstation2Buffer_C2 = buffer.Buffer(component=2, product=2, futureEvents=self.futureEvents)
        self.workstation2 = workstation.Workstation(buffers = [self.workstation2Buffer_C1,self.workstation2Buffer_C2], futureEvents=self.futureEvents)

        self.workstation3Buffer_C1 = buffer.Buffer(component=1, product=3, futureEvents=self.futureEvents)
        self.workstation3Buffer_C3 = buffer.Buffer(component=3, product=3, futureEvents=self.futureEvents)
        self.workstation3 = workstation.Workstation(buffers=[self.workstation3Buffer_C1, self.workstation3Buffer_C3], futureEvents=self.futureEvents)

        self.inspector1 = inspector.Inspector(components=[1], buffers=[self.workstation1Buffer, self.workstation2Buffer_C1, self.workstation3Buffer_C1], futureEvents=self.futureEvents)
        self.inspector2 = inspector.Inspector(components=[2,3], buffers=[self.workstation2Buffer_C2, self.workstation3Buffer_C3], futureEvents=self.futureEvents)

    def start(self):
        print("Starting Simulation")
        self.inspector1.start()
        self.inspector2.start()
