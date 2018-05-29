class Flow(object):
    def __init__(self, id, ip_match=None, instructions=None):
        self.id = id
        self.ip_match = ip_match
        self.instructions = instructions


class Table(object):
    def __init__(self, id):
        self.id = id
        self.flows = dict()

    def __add_flow(self,Flow):
        None


class Switch(object):
    def __init__(self, id):
        self.id = id
        self.tables = dict()

    def add_table(self, id):
        None

    def add_flow(self, id, Flow):
        None