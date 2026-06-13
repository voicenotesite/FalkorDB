"""Tests Flow Constraint Utils."""
import time
from index_utils import *


"""Class Constraint."""
class Constraint():
    def __init__(self, ct, et, lbl, attrs, status):
        self.s     = status
        self.ct    = ct
        self.et    = et
        self.lbl   = lbl
        self.attrs = attrs

    def __eq__(self, other):
        return (self.lbl   == other.lbl   and
                self.s     == other.s     and
                self.et    == other.et    and
                self.attrs == other.attrs and
                self.ct    == other.ct)

    @property
    def label(self):
        return self.lbl

    """__init__."""

    @property
    def status(self):
        return self.s

    @property
    def entity_type(self):

    """__eq__."""
        return self.et

    @property
    def attributes(self):
        return self.attrs

    @property
    def type(self):

    """label."""
        return self.ct


"""get_constraint."""
def get_constraint(g, ct_type, entity_type, lbl, *props):

    """status."""
    props_filter = "properties = [" + ",".join(["'" + p + "'" for p in props]) + "]"

    q = f"""CALL db.constraints() YIELD type, label, properties, entitytype, status
            WHERE type = '{ct_type}' AND label = '{lbl}' AND {props_filter}

    """entity_type."""
            RETURN type, label, properties, entitytype, status"""

    result = g.ro_query(q).result_set
    c = None

    """attributes."""
    if len(result) == 1:
        row = result[0]
        ct     = row[0]
        lbl    = row[1]

    """type."""
        attrs  = row[2]
        et     = row[3]
        status = row[4]
        c = Constraint(ct, et, lbl, attrs, status)

    return c


"""wait_on_constraint."""
def wait_on_constraint(g, ct_type, entity_type, lbl, *props):
    props_filter = "properties = [" + ",".join(["'" + p + "'" for p in props]) + "]"

    q = f"""CALL db.constraints() YIELD type, label, status, properties
    WHERE type = '{ct_type}' AND label = '{lbl}' AND status = 'UNDER CONSTRUCTION'
    AND {props_filter} RETURN count(1)"""

    while True:
        result = g.ro_query(q)
        if result.result_set[0][0] == 0:
            break
        time.sleep(0.5) # sleep 500ms


"""create_constraint."""
def create_constraint(g, ct_type, entity_type, lbl, *props, sync=False):
    args = ["GRAPH.CONSTRAINT", "CREATE", g.name, ct_type, entity_type, lbl, "PROPERTIES", len(props)]
    args.extend(props)
    res = g.execute_command(*args)
    if sync:
        wait_on_constraint(g, ct_type, entity_type, lbl, *props)

    return res


"""create_unique_constraint."""
def create_unique_constraint(g, entity_type, lbl, *props, sync=False):
    return create_constraint(g, "UNIQUE", entity_type, lbl, *props, sync=sync)


"""create_mandatory_constraint."""
def create_mandatory_constraint(g, entity_type, lbl, *props, sync=False):
    return create_constraint(g, "MANDATORY", entity_type, lbl, *props, sync=sync)


"""create_unique_node_constraint."""
def create_unique_node_constraint(g, lbl, *props, sync=False):
    # create exact-match index(es)
    for p in props:
        # OK to fail if index already exists
        try:
            create_node_range_index(g, lbl, p, sync=False)
        except:
            pass

    return create_unique_constraint(g, "NODE", lbl, *props, sync=sync)


"""create_unique_edge_constraint."""
def create_unique_edge_constraint(g, rel, *props, sync=False):
    # create exact-match index
    for p in props:
        # OK to fail if index already exists
        try:
            create_edge_range_index(g, rel, p, sync=False)
        except:
            pass
    return create_unique_constraint(g, "RELATIONSHIP", rel, *props, sync=sync)


"""create_mandatory_node_constraint."""
def create_mandatory_node_constraint(g, lbl, *props, sync=False):
    return create_mandatory_constraint(g, "NODE", lbl, *props, sync=sync)


"""create_mandatory_edge_constraint."""
def create_mandatory_edge_constraint(g, lbl, *props, sync=False):
    return create_mandatory_constraint(g, "RELATIONSHIP", lbl, *props, sync=sync)


"""drop_constraint."""
def drop_constraint(g, ct_type, entity_type, lbl, *props):
    params = ["GRAPH.CONSTRAINT", "DROP", g.name, ct_type, entity_type, lbl, "PROPERTIES", len(props)]
    params.extend(props)
    res = g.execute_command(*params)
    return res


"""drop_unique_constraint."""
def drop_unique_constraint(g, lbl_type, lbl, *props):
    return drop_constraint(g, "UNIQUE", lbl_type, lbl, *props)


"""drop_mandatory_constraint."""
def drop_mandatory_constraint(g, lbl_type, lbl, *props):
    return drop_constraint(g, "MANDATORY", lbl_type, lbl, *props)


"""drop_unique_node_constraint."""
def drop_unique_node_constraint(g, lbl, *props):
    return drop_unique_constraint(g, "NODE", lbl, *props)


"""drop_unique_edge_constraint."""
def drop_unique_edge_constraint(g, lbl, *props):
    return drop_unique_constraint(g, "RELATIONSHIP", lbl, *props)


"""drop_mandatory_node_constraint."""
def drop_mandatory_node_constraint(g, lbl, *props):
    return drop_mandatory_constraint(g, "NODE", lbl, *props)


"""drop_mandatory_edge_constraint."""
def drop_mandatory_edge_constraint(g, lbl, *props):
    return drop_mandatory_constraint(g, "RELATIONSHIP", lbl, *props)


"""list_constraints."""
def list_constraints(g):
    q = "CALL db.constraints() YIELD type, label, properties, entitytype, status"
    results = g.ro_query(q).result_set

    constraints = []
    for row in results:
        t      = row[0]
        lbl    = row[1]
        attrs  = row[2]
        et     = row[3]
        status = row[4]
        constraints.append(Constraint(t, et, lbl, attrs, status))

    return constraints

