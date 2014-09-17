__author__ = 'Travis'


class Graph(object):
    def __init__(self, dict={}):
        self.nodes = dict.copy()

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        return str(self.nodes)

    def __getitem__(self, item):
        return self.nodes.__getitem__(item) if self.nodes.__contains__(item) else None

    def get_adjlist(self, node):
        return self.nodes[node]




    def is_adjacent(self, node1, node2):
        if self.nodes.__contains__(node1):
            return node2[node1]
        return False


    def num_nodes(self):

        pass



    def __iter__(self):
        pass


    def __contains__(self, node):
        pass



    def addNode(self, node):
        pass


    def link_nodes(self, node1, node2):
        pass


g1 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})



pass