from event import Event
from inspector import Inspector
from buffer import Buffer
from workstation import Workstation

import queue
from simple_chalk import chalk

class Simulation:
    """docstring for Component."""

    def __init__(self, simulationRunTime, seed):
        super(Simulation, self).__init__()

        self.seed = seed
        self.currentTime = 0

        futureEvents = queue.PriorityQueue()
        futureEvents.put(Event(simulationRunTime, self, "end"))

        buffer_1_1 = Buffer(component=1, product=1, futureEvents=futureEvents)
        workstation1 = Workstation(name="Workstation 1", buffers=[buffer_1_1], product=1, futureEvents=futureEvents, log=self.log)

        buffer_2_1 = Buffer(component=1, product=2, futureEvents=futureEvents)
        buffer_2_2 = Buffer(component=2, product=2, futureEvents=futureEvents)
        workstation2 = Workstation(name="Workstation 2", buffers = [buffer_2_1,buffer_2_2], product=2, futureEvents=futureEvents, log=self.log)

        buffer_3_1 = Buffer(component=1, product=3, futureEvents=futureEvents)
        buffer_3_3 = Buffer(component=3, product=3, futureEvents=futureEvents)
        workstation3 = Workstation(name="Workstation 3", buffers=[buffer_3_1, buffer_3_3], product=3, futureEvents=futureEvents, log=self.log)

        inspector1 = Inspector(name="Inspector 1", components=[1], buffers=[buffer_1_1, buffer_2_1, buffer_3_1], futureEvents=futureEvents, log=self.log)
        inspector2 = Inspector(name="Inspector 2", components=[2,3], buffers=[buffer_2_2, buffer_3_3], futureEvents=futureEvents, log=self.log)

        self.pastEvents = list()
        self.futureEvents = futureEvents
        self.inspectors = [inspector1, inspector2]
        self.buffers = [buffer_1_1, buffer_2_1, buffer_2_2, buffer_3_1, buffer_3_3]
        self.workstations = [workstation1, workstation2, workstation3]


    def start(self):
        self.log(chalk.cyan("Starting Simulation"))
        self.inspectors[0].start()
        self.inspectors[1].start()

        currentEvent = self.futureEvents.get()
        while currentEvent.action != "end":
            currentEvent.action(self.currentTime)

            self.pastEvents.append(currentEvent)
            currentEvent = self.futureEvents.get()
            self.currentTime = currentEvent.time
        self.log(chalk.cyan("Simulation Complete"))

    def log(self, message):
        timeString = "{:7.3f}m".format(self.currentTime)
        print(chalk.bgGreen(timeString) + " " + message)
