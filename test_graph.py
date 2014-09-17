from unittest import TestCase

__author__ = 'Travis'
import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.emp = Graph()
        self.big = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
        self.a = Graph({'A': []})
        self.aB = Graph({'A': ['B']})
        self.aBD = Graph({'A': ['B','D']})
        self.bC = Graph({'B': ['C']})
        self.aBbA = Graph({'A': ['B'], 'B': ['A']})
        self.aBbAc = Graph({'A': ['B'], 'B': ['A'], 'C': []})
        self.aBbAc = Graph({'A': ['B'], 'B': ['A'], 'C': ['A','B']})



    def test_is_adjacent(self):
        #self.assertTrue(g1.h)
        self.fail()





if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)


