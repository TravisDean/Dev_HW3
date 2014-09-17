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



    def test_get_adjlist_q1(self):
        g = self.a
        v = 'A'
        exp = []
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)

    def test_get_adjlist_q2(self):
        g = self.aBD
        v = 'A'
        exp = ['B','D']
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)

    def test_get_adjlist_q3(self):
        g = self.emp
        v = ''
        exp = None
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)

    def test_is_adjacent_correct_q4(self):
        g = self.aBD
        v = ('A','B')
        res = g.is_adjacent(*v)
        self.assertTrue(res)




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)


