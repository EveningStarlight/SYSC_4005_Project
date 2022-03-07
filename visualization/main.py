from data import Data
from visulization import Visulization

import sys

if __name__ == '__main__':

    version = int(sys.argv[1]) if len(sys.argv) > 1 else "v1.0"


    visulization = Visulization(Data.getData(version))
    visulization.createHistograms()
