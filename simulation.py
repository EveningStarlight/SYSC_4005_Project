import event
import inspector
import buffer
import workstation

class Simulation(Object):
    """docstring for Component."""

    def __init__(self, simulationTime):
        super(Simulation, self).__init__()

        self.futureEvents = queue.PriorityQueue()
        self.futureEvents.put(Event(SIMULATION_TIME, , "end"))

        self.workstation1Buffer = Buffer(component=1, product=1)
        self.workstation1 = Workstation(buffers=[workstation1Buffer])

        self.workstation2Buffer_C1 = Buffer(component=1, product=2)
        self.workstation2Buffer_C2 = Buffer(component=2, product=2)
        self.workstation2 = Workstation(buffers = [workstation2Buffer_C1,workstation2Buffer_C2])

        self.workstation3Buffer_C1 = Buffer(component=1, product=3)
        self.workstation3Buffer_C3 = Buffer(component=3, product=3)
        self.workstation3 = Workstation(buffers=[workstation3Buffer_C1, workstation3Buffer_C3])

        self.inspector1 = Inspector(components=[1], buffers=[workstation1Buffer, workstation2Buffer_C1, workstation3Buffer_C1])
        self.inspector2 = Inspector(components=[2,3], buffers=[workstation2Buffer_C2, workstation3Buffer_C3])

    def start(self):
        self.inspector1.start()
        self.inspector2.start()
