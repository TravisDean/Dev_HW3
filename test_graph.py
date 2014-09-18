__author__ = 'tjd2qj'
import unittest

from graph import Graph

# noinspection PyPep8Naming
class TestGraph(unittest.TestCase):
    """Allows testing of all functions of our graph class."""
    def setUp(self):
        self.emp = Graph()
        self.big = Graph({'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E': []})
        self.a = Graph({'A': []})
        self.ac = Graph({'A': [], 'C': []})
        self.aB = Graph({'A': ['B']})
        self.aBD = Graph({'A': ['B', 'D']})
        self.bC = Graph({'B': ['C']})
        self.aBbA = Graph({'A': ['B'], 'B': ['A']})
        self.aBbAc = Graph({'A': ['B'], 'B': ['A'], 'C': []})
        self.aBbAcAB = Graph({'A': ['B'], 'B': ['A'], 'C': ['A', 'B']})
        self.aBCbAcA = Graph({'A': ['B', 'C'], 'B': ['A'], 'C': ['A']})
        self.aBbC = Graph({'A': ['B'], 'B': ['C']})

    # region get_adj_testing
    def test_get_adjlist_q1(self):
        g = self.a
        v = 'A'
        exp = []
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)

    def test_get_adjlist_q2(self):
        g = self.aBD
        v = 'A'
        exp = ['B', 'D']
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)

    def test_get_adjlist_q3(self):
        g = self.emp
        v = ''
        exp = None
        res = g.get_adjlist(v)
        self.assertEqual(res, exp)
    # endregion

    # region is_adj_test
    def test_is_adjacent_q4(self):
        g = self.aBD
        v = ('A', 'B')
        res = g.is_adjacent(*v)
        self.assertTrue(res)

    def test_is_adjacent_q5(self):
        g = self.aBD
        v = ('B', 'A')
        res = g.is_adjacent(*v)
        self.assertFalse(res)

    def test_is_adjacent_q6(self):
        g = self.emp
        v = ('B', 'A')
        res = g.is_adjacent(*v)
        self.assertFalse(res)

    # endregion
    #region num_nodes
    def test_num_nodes_q7(self):
        g = self.emp
        res = g.num_nodes()
        self.assertEqual(res, 0)


    def test_num_nodes_q8(self):
        g = self.big
        res = g.num_nodes()
        self.assertEqual(res, 5)

    #endregion
    #region contains
    def test_contains_q9(self):
        g = self.aBD
        v = 'A'
        res = g.__contains__(v)
        self.assertTrue(res)

    def test_contains_q10(self):
        g = self.aBD
        v = 'B'
        res = g.__contains__(v)
        self.assertFalse(res)

    #endregion
    #region len
    def test_len_q11(self):
        g = self.emp
        res = len(g)
        self.assertEqual(res, 0)

    def test_len_q12(self):
        g = self.aBbAc
        res = len(g)
        self.assertEqual(res, 3)

    #endregion

    #region add_node
    def test_addNode_q13(self):
        g = self.emp
        v = 'A'
        res = g.addNode(v)
        self.assertTrue(res)

    def test_addNode_q14(self):
        g = self.aBD
        v = 'A'
        res = g.addNode(v)
        self.assertFalse(res)

    def test_addNode_q15(self):
        g = self.bC
        v = 'A'
        res = g.addNode(v)
        self.assertTrue(res)
        self.assertEqual(g.get_adjlist('A'), [])

    #endregion

    #region link_nodes
    def test_link_nodes_q16(self):
        """Checking for already adj links"""
        g = self.aBbA
        v = ('A', 'B')
        res = g.link_nodes(*v)
        self.assertFalse(res)

    def test_link_nodes_q17(self):
        """Test to make sure that the nodes were added correctly."""
        g = self.aBbAc
        v = ('A', 'C')
        res = g.link_nodes(*v)
        self.assertTrue(res)
        self.assertEqual(g.nodes, self.aBCbAcA.nodes)

    def test_link_nodes_q18(self):
        g = self.aBbA
        v = ('A', 'A')
        res = g.link_nodes(*v)
        self.assertFalse(res)

    def test_link_nodes_q19(self):
        """Test for nodes not in the graph to fail"""
        g = self.ac
        v = ('A', 'B')
        res = g.link_nodes(*v)
        self.assertFalse(res)

    #endregion

    #region unlink_nodes
    def test_unlink_nodes_q20(self):
        """Unlinking nodes not intially adj returns false.


        """
        g = self.aBbC
        v = ('A', 'B')
        res = g.unlink_nodes(*v)
        self.assertFalse(res)

    def test_unlink_nodes_q21(self):
        """Insure that unlinking nodes not in the graph returns False.


        """
        g = self.aB
        v = ('A', 'B')
        res = g.unlink_nodes(*v)
        self.assertFalse(res)

    def test_unlink_nodes_q22(self):
        """Require that unlinking nodes actually unlinkes them, and not others.


        """
        g = self.aBbA
        v = ('A', 'B')
        res = g.unlink_nodes(*v)
        self.assertTrue(res)

    #endregion

    #region del_node
    def test_del_node_q23(self):
        g = self.aB
        v = 'C'
        res = g.del_node(v)
        self.assertFalse(res)

    def test_del_node_q24(self):
        g = self.aBbAcAB
        v = 'B'
        res = g.del_node(v)
        self.assertTrue(res)
        self.assertDictEqual(g.nodes, {'A': [], 'C': ['A']})
    #endregion


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)


