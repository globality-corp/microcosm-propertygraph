"""
Node store tests.

"""
from hamcrest import (
    assert_that,
    contains,
    equal_to,
    has_properties,
    is_,
)

from microcosm_propertygraph.stores.node_store import NaiveNodeStore


class ExampleNodeStore(NaiveNodeStore):

    def iter_items(self, **kwargs):
        yield self.model_class(
            id="1",
            labels=["label"],
            properties={},
        )
        yield self.model_class(
            id="2",
            labels=["label"],
            properties={},
        )
        yield self.model_class(
            id="3",
            labels=["label"],
            properties={},
        )


class TestNodeStore:

    def setup(self):
        self.store = ExampleNodeStore()

    def test_count(self):
        assert_that(self.store.count(), is_(equal_to(3)))

    def test_search(self):
        assert_that(
            self.store.search(),
            contains(
                has_properties(id="1"),
                has_properties(id="2"),
                has_properties(id="3"),
            ),
        )

    def test_search_limit(self):
        assert_that(
            self.store.search(limit=1),
            contains(
                has_properties(id="1"),
            ),
        )

    def test_search_offset(self):
        assert_that(
            self.store.search(offset=1),
            contains(
                has_properties(id="2"),
                has_properties(id="3"),
            ),
        )

    def test_search_offset_limit(self):
        assert_that(
            self.store.search(offset=1, limit=1),
            contains(
                has_properties(id="2"),
            ),
        )
