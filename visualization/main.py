from data import Data
from visulization import Visulization
from stats import Stats

import sys

if __name__ == '__main__':
    version = int(sys.argv[1]) if len(sys.argv) > 1 else "v1.0"

    data = Data.getData(version)

    #stats = Stats(data)
    #stats.printStats()

    visulization = Visulization(data)
    #visulization.createHistograms()
    #visulization.createQQs()
    #visulization.createChi2s()
    visulization.createScatter()
