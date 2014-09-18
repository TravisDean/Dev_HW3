__author__ = 'tjd2qj'
import unittest
from graph import Graph
from graph_functions import is_complete, nodes_by_degree

class TestGraphFuncs(unittest.TestCase):
    """Allows testing of external functions of our graph class."""
    def setUp(self):
        self.abc = Graph({'A': ['B'], 'B': ['C'],'C':['A']})
        self.ab = Graph({'A': ['B'], 'B': ['C'],'C':[]})
        self.num = Graph({1: [1,2,3,4], 5:[1,2], 3:[1,2,3]})

    def test_is_complete(self):
        self.assertTrue(is_complete(self.abc))

    def test_is_incomplete(self):
        self.assertFalse(is_complete(self.ab))

    def test_node_deg(self):
        exp = [('A', 1), ('C', 1), ('B', 1)]
        self.assertEqual(nodes_by_degree(self.abc), exp)
        exp = [(1, 4), (3,3), (5,2)]
        self.assertEqual(nodes_by_degree(self.num), exp)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraphFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)
