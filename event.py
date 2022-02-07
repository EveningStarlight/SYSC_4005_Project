class Event(Object):
    """docstring for Component."""

    def __init__(self, eventTime, eventCaller, eventAction):
        super(Event, self).__init__()
        self.time = eventTime
        self.caller = eventCaller
        self.action = eventAction

    def __lt__(self, other):
        return self.time < other.time
