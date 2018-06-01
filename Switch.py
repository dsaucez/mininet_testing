class Flow(object):
    def __init__(self, id, priority="1", name="None", ipv4=None, instruction=None):
        self.id = id
        self.priority = priority
        self.name = name
        self.ipv4 = ipv4
        self.instruction = instruction


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
        self.links = set()
        self.port_mapping = dict()

    def add_link(self, s1, s2, port=None):
        if s1 == self.id or s2 == self.id:
            if not((s1, s2) in self.links or (s2, s1) in self.links):
                self.links.add((s1, s2))
                if s1 == self.id:
                    self.__add_link_port_map(s2, port)
                else:
                    self.__add_link_port_map(s1, port)

    def __add_link_port_map(self, dest_switch, port):
        self.port_mapping[dest_switch] = port

    def get_port(self, dest_switch):
        if self.check_link(self.id, dest_switch):
            return self.port_mapping[dest_switch]
        else:
            raise KeyError("the link ({},{}) does not exist".format(self.id, dest_switch))


    def remove_link(self, s1, s2):
        if (s1, s2) in self.links:
            self.links.remove((s1, s2))
        if (s2, s1) in self.links:
            self.links.remove((s2, s1))

    def check_link(self, s1, s2):
        return (s1, s2) in self.links or (s2, s1) in self.links

    def add_table(self, table_id):
        if str(table_id) in self.tables.keys():
            raise DuplicatedKeyError("Table with id {} already exist".format(table_id))
        else:
            self.tables[table_id] = Table(table_id)

    def add_flow(self, table_id, flow):
        if not (table_id in self.tables.keys()):
            self.add_table(table_id)
        self.tables[table_id].add_flow(flow)

    def remove_flow(self, table_id, flow_id):
        if not (table_id in self.tables.keys()):
            raise KeyError("{} does not exist in switch {}".format(table_id, self.id))
        if not (flow_id in self.tables[table_id].flows):
            raise KeyError("{} does not exist in table {}".format(flow_id, table_id))
        del self.tables[table_id].flows[flow_id]

    def __str__(self):
        return "id : {}, tables : {}".format(self.id, str(self.tables))


class DuplicatedKeyError(ValueError):
    def __init__(self, message, errors=None):
        super(DuplicatedKeyError, self).__init__(message)
        self.errors = errors
