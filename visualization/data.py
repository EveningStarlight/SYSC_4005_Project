import os

class Data:
    newestVersion = "v1.0"

    def getData(version):
        data = Data.getDataObject(version)

        parentDirect = os.path.split(os.path.dirname(__file__))[0]
        directory = os.path.join(parentDirect, 'stats')
        if os.path.exists(directory):
            for file in os.listdir(directory):
                filePath = os.path.join(directory, file)
                lines = open(filePath).readlines()
                if lines.pop(0).strip() == version:
                    for line in lines:
                        line = line.strip()
                        k, v = line.split(": ")
                        data[k]['data'].append(float(v))

        return data

    def getDataObject(version):
        if version == "v1.0":
            data = {
            "Inspector 1 percent busy": Data.percentBusy(),
            "Inspector 2 percent busy": Data.percentBusy(),
            "Workstation 1 percent busy": Data.percentBusy(),
            "Workstation 2 percent busy":  Data.percentBusy(),
            "Workstation 3 percent busy":  Data.percentBusy(),
            "Workstation 1 parts per minute": Data.partsPerMin(),
            "Workstation 2 parts per minute": Data.partsPerMin(),
            "Workstation 3 parts per minute": Data.partsPerMin(),
            "Factory parts per minute": Data.partsPerMin(),
            "Buffer 1-1 average occupancy": Data.averageComponents(),
            "Buffer 2-1 average occupancy": Data.averageComponents(),
            "Buffer 2-2 average occupancy": Data.averageComponents(),
            "Buffer 3-1 average occupancy": Data.averageComponents(),
            "Buffer 3-3 average occupancy": Data.averageComponents(),
            }
        else:
            raise ValueError("Version number not found")

        for k in data.keys():
            data[k]['name'] = k

        return data

    def percentBusy():
        return {
            'data':[],
            'histMin': 0,
            'histMax': 100,
             }

    def partsPerMin():
        return {
            'data':[],
            'histMin': 0,
            'histMax': None,
             }

    def averageComponents():
        return {
            'data':[],
            'histMin': 0,
            'histMax': 2,
             }
