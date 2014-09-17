__author__ = 'tjd2qj'


class Graph(object):
    def __init__(self, d={}):
        self.nodes = d.copy() or {}

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        return str(self.nodes)

    def __getitem__(self, item):
        """
        :rtype : list
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


    def __iter__(self):
        return iter(self)


    def __contains__(self, node):
        return node in self.nodes


    # noinspection PyPep8Naming
    def addNode(self, node):
        if node in self.nodes: return False
        self.nodes[node] = []
        return True

    def del_node(self, node):
        ret = False
        for v in self.nodes.values():
            if node in v:
                v.remove(node)
                ret = True
        if node in self.nodes.copy():
            del self.nodes[node]
            ret = True
        return ret


    def link_nodes(self, node1, node2):
        if node1 not in self.nodes or node2 in self.nodes[node1] or node2 not in self.nodes or node1 in self.nodes[
            node2] or node1 is node2: return False

        self.nodes[node1] += node2
        self.nodes[node2] += node1
        return True

    def unlink_nodes(self, node1, node2):
        if self.nodes.__contains__(node1 and node2):
            if self.is_adjacent(node1, node2) and self.is_adjacent(node2, node1):
                self.nodes[node1].remove(node2)
                self.nodes[node2].remove(node1)
                return True
        return False


g2 = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
