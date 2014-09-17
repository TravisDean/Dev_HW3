__author__ = 'Travis'


class Graph(object):
    def __init__(self, dict={}):
        self.nodes = dict.copy()

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        return str(self.nodes)

    def __getitem__(self, item):
        """


        :rtype : object
        :param item:
        :return:
        """
        return self.nodes[item]

    def get_adjlist(self, node):
        if node in self.nodes:
            return self.nodes[node]





    def is_adjacent(self, node1, node2):
        if not node1 in self.nodes: return False
        if node2 in self.nodes[node1]: return True
        return False


    def num_nodes(self):
        return len(self.nodes)
        pass



    def __iter__(self):
        return iter(self)
        pass


    def __contains__(self, node):
        return node in self.nodes



    def addNode(self, node):
        pass


    def link_nodes(self, node1, node2):
        pass


g1 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
