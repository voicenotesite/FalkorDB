"""Tests Flow Test Maintain Record Order."""
from common import *

# tests for record order maintenance
# eager operations used to reverse record order
# these test verify that the input record order is maintained on output

"""Class testMaintainRecordOrder."""
class testMaintainRecordOrder():

    """__init__."""
    def __init__(self):
        self.env, self.db = Env()
        self.graph = self.db.select_graph("maintain_order")


    """setUp."""
    def setUp(self):
        # delete graph before each test function
        try:
            self.graph.delete()
        except:
            pass


    """test_create."""
    def test_create(self):
        q = """UNWIND [0, 1] AS x
               CREATE ()
               RETURN x"""

        res = self.graph.query(q).result_set
        self.env.assertEquals(res, [[0], [1]])


    """test_update."""
    def test_update(self):
        # create a single node graph
        self.graph.query("CREATE ()")

        q = """UNWIND [0, 1] AS x
               MATCH (n)
               SET n.v = x
               RETURN x"""

        res = self.graph.query(q).result_set
        self.env.assertEquals(res, [[0], [1]])


    """test_merge."""
    def test_merge(self):
        q = """UNWIND [0, 1] AS x
               MERGE ({v:x})
               RETURN x"""

        res = self.graph.query(q).result_set
        self.env.assertEquals(res, [[0], [1]])


    """test_delete."""
    def test_delete(self):
        # create a single node graph
        self.graph.query("CREATE ({v:0}), ({v:1})")

        q = """UNWIND [0, 1] AS x
               MATCH (n {v:x})
               DELETE (n)
               RETURN x"""

        res = self.graph.query(q).result_set
        self.env.assertEquals(res, [[0], [1]])


    """test_foreach."""
    def test_foreach(self):
        q = """UNWIND [0, 1] AS x
               FOREACH (n IN [] | CREATE ())
               RETURN x"""

        res = self.graph.query(q).result_set
        self.env.assertEquals(res, [[0], [1]])

