"""
Test the Node model.

"""
from hamcrest import assert_that, has_properties

from microcosm_propertygraph.models.node import Node


def test_node_model():
    node_id = "AbCdEf123456789"
    labels = ["foo", "bar"]
    properties = dict(baz=["value_1", "value_2"])
    assert_that(
        Node(
            id=node_id,
            labels=labels,
            properties=properties,
        ),
        has_properties(
            id=node_id,
            labels=labels,
            properties=properties,
        ),
    )
