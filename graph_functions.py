__author__ = 'tjd2qj'
from graph import Graph
from itertools import chain


def is_complete(grph):
    """Test if the graph is a completely connected graph.
    :rtype : bool
    :type grph: Graph
    """
    if not isinstance(grph, Graph): raise TypeError
    if len(grph) <= 1: return True
   
    ke = _flat(grph.nodes.keys())
    ve = _flat(grph.nodes.values())

    return  True if ke <= ve else False

def nodes_by_degree(grph):
    lst =  [(k, len(grph[k])) for k in grph.nodes.keys()]
    s = sorted(lst, key=lambda l:l[1], reverse=True)
    return s






def _flat(seq):
    return set(chain(*seq))


def test():
    abc = Graph({'A': ['B'], 'B': ['C'],'C':['A']})
    ab = Graph({'A': ['B'], 'B': ['C'],'C':[]})

    print(is_complete(abc))
    print(is_complete(ab))

if __name__ == "__main__": test()

        



