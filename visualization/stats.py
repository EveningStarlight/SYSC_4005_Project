import numpy as np
import statsmodels.stats.api as sms
from statistics import NormalDist
import math

class Stats:

    def __init__(self, data):
        self.data = data
        self.getStats()

    def getStats(self):
        keys = self.data.keys()
        for key in keys:
            data = self.data[key]["data"]
            self.data[key]["NormalDist"] = NormalDist.from_samples(data)

    def printStats(self):
        keys = self.data.keys()
        for key in keys:
            format = self.data[key]["format"]
            dist = self.data[key]["NormalDist"]

            ICDF = 0 if dist.stdev == 0 else format(dist.inv_cdf(p=0.95)-dist.mean)
            CI = 2.575*dist.stdev/math.sqrt(len(self.data[key]["data"]))
            CI = 0 if dist.stdev == 0 else format(CI)
            mean = format(dist.mean)
            print(key, "mean is: ", mean, "±", CI, ", ICDF ", ICDF)
