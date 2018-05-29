class Flow(object):
    def __init__(self, id, ip_match=None, instructions=None):
        self.id = id
        self.ip_match = ip_match
        self.instructions = instructions


class Table(object):
    def __init__(self, id):
        self.id = id
        self.flows = dict()

    def add_flow(self, flow):
        if not (type(flow) is Flow):
            raise TypeError("flow is not Flow type")
        if flow.id in self.flows.keys():
            raise DuplicatedKeyError("Flow with id {} already exist", flow.id)
        self.flows[flow.id] = Flow(flow.id)


class Switch(object):
    def __init__(self, id):
        self.id = id
        self.tables = dict()

    def add_table(self, id):
        if str(id) in self.tables.keys():
            raise DuplicatedKeyError("Table with id {} already exist".format(id), id)
        else:
            self.tables[id] = Table(id)

    def add_flow(self, table_id, flow):
        if not (table_id in self.tables.keys()):
            self.add_table(table_id)
        self.tables[table_id].add_flow(flow)

    def remove_flow(self,table_id, flow_id):
        if not (table_id in self.tables.keys()):
            raise KeyError("{} does not exist in this switch", table_id)
        if not (flow_id in self.tables[table_id]):
            raise KeyError("{} does not exist in this table", flow_id)
        del self.tables[table_id][flow_id]

    def __str__(self):
        return "id : {}, tables : {}".format(self.id, str(self.tables))

class DuplicatedKeyError(ValueError):
    def __init__(self, message, errors=None):
        super(DuplicatedKeyError, self).__init__(message)
        self.errors = errors