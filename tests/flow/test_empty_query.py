"""Tests Flow Test Empty Query."""
from common import *


"""Class testEmptyQuery."""
class testEmptyQuery(FlowTestsBase):

    """__init__."""
    def __init__(self):
        self.env, self.db = Env()
        self.graph = self.db.select_graph('G')


    """test01_empty_query."""
    def test01_empty_query(self):
        try:
            # execute empty query
            self.graph.query("")
        except ResponseError as e:
            self.env.assertIn("Error: empty query.", str(e))


    """test02_whitespace_and_semicolon_queries."""
    def test02_whitespace_and_semicolon_queries(self):
        for query in [" ", ";"]:
            try:
                self.graph.query(query)
                self.env.assertTrue(False)
            except ResponseError as e:
                self.env.assertIn("Error: empty query.", str(e))

    #def test02_query_with_only_params(self):
    #    try:
    #        self.graph.query("CYPHER v=1")
    #    except ResponseError as e:
    #        self.env.assertIn("Error: could not parse query", str(e))
