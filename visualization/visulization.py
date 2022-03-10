import matplotlib.pyplot as plt
import statsmodels.api as sm
import math

class Visulization:

    def __init__(self, data):
        self.data = data

    def createHistograms(self):
        keys = self.data.keys()

        fig, axs = plt.subplots(math.ceil(len(keys)/3), 3)
        pos = 0
        for key in keys:
            row = math.floor(pos/3)
            col = pos%3

            self.createHistogram(key, axs[row, col])
            pos += 1

        plt.show()

    def createHistogram(self, key, ax):
        data = self.data[key]

        ax.hist(data['data'])
        ax.set_title(data['name'])

    def createQQs(self):
        keys = self.data.keys()

        fig = sm.qqplot(keys, line='45')

        plt.show()



