import event

class Workstation(object):
    """docstring for Workstation."""

    def __init__(self, buffers, product, futureEvents):
        super(Workstation, self).__init__()
        self.buffers = buffers
        self.product = product
        self.futureEvents = futureEvents
