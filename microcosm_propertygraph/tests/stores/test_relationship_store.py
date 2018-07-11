"""
Relationship store tests.

"""
from hamcrest import (
    assert_that,
    contains,
    equal_to,
    has_properties,
    is_,
)

from microcosm_propertygraph.stores.relationship_store import NaiveRelationshipStore


class ExampleRelationshipStore(NaiveRelationshipStore):

    def iter_items(self, **kwargs):
        yield self.model_class(
            start_id="1",
            end_id="2",
            type=["foo"],
            properties={},
        )
        yield self.model_class(
            start_id="2",
            end_id="3",
            type=["foo"],
            properties={},
        )
        yield self.model_class(
            start_id="3",
            end_id="1",
            type=["foo"],
            properties={},
        )


class TestRelationshipStore:

    def setup(self):
        self.store = ExampleRelationshipStore()

    def test_count(self):
        assert_that(self.store.count(), is_(equal_to(3)))

    def test_search(self):
        assert_that(
            self.store.search(),
            contains(
                has_properties(start_id="1"),
                has_properties(start_id="2"),
                has_properties(start_id="3"),
            ),
        )

    def test_search_limit(self):
        assert_that(
            self.store.search(limit=1),
            contains(
                has_properties(start_id="1"),
            ),
        )

    def test_search_offset(self):
        assert_that(
            self.store.search(offset=1),
            contains(
                has_properties(start_id="2"),
                has_properties(start_id="3"),
            ),
        )

    def test_search_offset_limit(self):
        assert_that(
            self.store.search(offset=1, limit=1),
            contains(
                has_properties(start_id="2"),
            ),
        )
