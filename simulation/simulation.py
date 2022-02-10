from event import Event
from inspector import Inspector
from buffer import Buffer
from workstation import Workstation

import random
import queue
import os.path
from simple_chalk import chalk

class Simulation:
    """docstring for Component."""
        
    def __init__(self, simulationRunTime, seed):
        super(Simulation, self).__init__()

        self.seed = seed
        self.currentTime = 0
        
        inspector1Times = list()
        inspector22Times = list()
        inspector23Times = list()
        workstation1Times = list()
        workstation2Times = list()
        workstation3Times = list()
        
        path = os.path.abspath(os.path.dirname(__file__))
        
        insp1TimesFile = open(os.path.join(path,'../data/servinsp1.dat'))
        for line in insp1TimesFile:
            inspector1Times.append(float(line))
        insp1TimesFile.close()
        random.Random(self.seed).shuffle(inspector1Times)
        
        insp22TimesFile = open(os.path.join(path,'../data/servinsp22.dat'))
        for line in insp22TimesFile:
            inspector22Times.append(float(line))
        insp22TimesFile.close()
        random.Random(self.seed).shuffle(inspector22Times)
        
        insp23TimesFile = open(os.path.join(path,'../data/servinsp23.dat'))
        for line in insp23TimesFile:
            inspector23Times.append(float(line))
        insp23TimesFile.close()
        random.Random(self.seed).shuffle(inspector23Times)
        
        ws1TimesFile = open(os.path.join(path,'../data/ws1.dat'))
        for line in ws1TimesFile:
            workstation1Times.append(float(line))
        ws1TimesFile.close()
        random.Random(self.seed).shuffle(workstation1Times)
        
        ws2TimesFile = open(os.path.join(path,'../data/ws2.dat'))
        for line in ws2TimesFile:
            workstation2Times.append(float(line))
        ws2TimesFile.close()
        random.Random(self.seed).shuffle(workstation2Times)
        
        ws3TimesFile = open(os.path.join(path,'../data/ws3.dat'))
        for line in ws3TimesFile:
            workstation3Times.append(float(line))
        ws3TimesFile.close()
        random.Random(self.seed).shuffle(workstation3Times)
  
        
        futureEvents = queue.PriorityQueue()
        futureEvents.put(Event(simulationRunTime, self, "end"))

        blockedQueue = queue.PriorityQueue()


        buffer_1_1 = Buffer(component=1, product=1, futureEvents=futureEvents)
        workstation1 = Workstation(name="Workstation 1", buffers=[buffer_1_1], product=1, futureEvents=futureEvents, blockedQueue=blockedQueue, log=self.log, times=workstation1Times, seed=self.seed)

        buffer_2_1 = Buffer(component=1, product=2, futureEvents=futureEvents)
        buffer_2_2 = Buffer(component=2, product=2, futureEvents=futureEvents)
        workstation2 = Workstation(name="Workstation 2", buffers = [buffer_2_1,buffer_2_2], product=2, futureEvents=futureEvents, blockedQueue=blockedQueue, log=self.log, times=workstation2Times, seed=self.seed)

        buffer_3_1 = Buffer(component=1, product=3, futureEvents=futureEvents)
        buffer_3_3 = Buffer(component=3, product=3, futureEvents=futureEvents)
        workstation3 = Workstation(name="Workstation 3", buffers=[buffer_3_1, buffer_3_3], product=3, futureEvents=futureEvents, blockedQueue=blockedQueue, log=self.log, times=workstation3Times, seed=self.seed)

        inspector1 = Inspector(name="Inspector 1", components=[1], buffers=[buffer_1_1, buffer_2_1, buffer_3_1], futureEvents=futureEvents, blockedQueue=blockedQueue, log=self.log, times=inspector1Times, seed=self.seed)
        inspector2Times = [inspector22Times, inspector23Times]
        inspector2 = Inspector(name="Inspector 2", components=[2,3], buffers=[buffer_2_2, buffer_3_3], futureEvents=futureEvents, blockedQueue=blockedQueue, log=self.log, times=inspector2Times, seed=self.seed)

        self.pastEvents = list()
        self.futureEvents = futureEvents
        self.blockedQueue = blockedQueue
        self.inspectors = [inspector1, inspector2]
        self.buffers = [buffer_1_1, buffer_2_1, buffer_2_2, buffer_3_1, buffer_3_3]
        self.workstations = [workstation1, workstation2, workstation3]


    def start(self):
        self.log(chalk.cyan("Starting Simulation"))
        self.inspectors[0].start()
        self.inspectors[1].start()
        self.workstations[0].start()
        self.workstations[1].start()
        self.workstations[2].start()

        currentEvent = self.futureEvents.get()
        while currentEvent.action != "end":
            currentEvent.action(self.currentTime)

            self.pastEvents.append(currentEvent)

            blockedEvents = list(self.blockedQueue.queue)
            self.blockedQueue.queue.clear()
            for event in blockedEvents:
                event.action(self.currentTime)

            currentEvent = self.futureEvents.get()
            self.currentTime = currentEvent.time
        self.log(chalk.cyan("Simulation Complete"))

        self.inspectors[0].end(self.currentTime)
        self.inspectors[1].end(self.currentTime)
        self.workstations[0].end(self.currentTime)
        self.workstations[1].end(self.currentTime)
        self.workstations[2].end(self.currentTime)

    def log(self, message):
        timeString = "{:7.3f}m".format(self.currentTime)
        print(chalk.bgGreen(timeString) + " " + message)
    
    
