"""
Test the Node model.

"""
from hamcrest import assert_that, has_properties

from microcosm_propertygraph.models.relationship import Relationship


def test_relationship_model():
    start_id = "ABC"
    end_id = "DEF"
    type = "RELATION_TYPE"
    properties = dict(baz=["value_1", "value_2"])
    assert_that(
        Relationship(
            start_id=start_id,
            end_id=end_id,
            type=type,
            properties=properties,
        ),
        has_properties(
            start_id=start_id,
            end_id=end_id,
            type=type,
            properties=properties,
        ),
    )
