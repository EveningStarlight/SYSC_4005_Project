import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
import statistics
import math
import numpy as np

class Visulization:

    def __init__(self, data):
        self.data = data

    def createScatter(self):
        keys = self.data.keys()

        for key in keys:
            x = []
            y = []
            for item in self.data[key]['data']:
                y.append(item[0])
                x.append(item[1])
            plt.scatter(x,y)
            plt.title(key)
            plt.xlabel('time (min)')
            plt.show()


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

        fig, axs = plt.subplots(math.ceil(len(keys)/3), 3)
        pos = 0
        for key in keys:
            row = math.floor(pos/3)
            col = pos%3

            self.createQQ(key,axs[row, col])
            pos += 1

        plt.show()

    def createQQ(self, key, ax):
        data = self.data[key]

        X = np.array(data['data'])
        fig = sm.qqplot(X, line='45', fit=True, dist=stats.norm)
        ax.set_title(data['name'])


    def createChi2s(self):
        keys = self.data.keys()

        for key in keys:
            self.createChi2(key)

    def createChi2(self, key):
        data = self.data[key]
        X = np.array(data['data'])
        mean = statistics.mean(X)
        sigma = statistics.stdev(X)
        X_normal = np.random.normal(mean, sigma, 100)

        value = np.concatenate((X,X_normal))

        p, dof = stats.chisquare(value)

        alpha = 0.1
        print(data['name'])
        print("p value is " + str(p))
        if p <= alpha:
            print('Dependent (reject H0)')
        else:
            print('Independent (H0 holds true)')
