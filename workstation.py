import event

class Workstation:
    """docstring for Workstation."""

    def __init__(self, buffers, product, futureEvents):
        super(Workstation, self).__init__()
        self.buffers = buffers
        self.product = product
        self.futureEvents = futureEvents
