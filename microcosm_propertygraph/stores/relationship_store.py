"""
Relationship persistence.

"""
from abc import ABCMeta, abstractmethod
from itertools import islice

from microcosm.api import binding
from microcosm_postgres.store import Store

from miranda.models.relationship import Relationship


@binding("relationship_store")
class RelationshipStore(Store, metaclass=ABCMeta):

    def __init__(self, graph, model_class=Relationship):
        super(RelationshipStore, self).__init__(graph, model_class)
        self.assertion_store = graph.assertion_store
        self.inferred_assertion_store = graph.inferred_assertion_store

    def count(self, **kwargs):
        return sum(1 for n in self.iter_relationships(**kwargs))

    def search(self, offset, limit, **kwargs):
        return islice(
            self.iter_relationships(**kwargs),
            offset,
            limit,
        )

    @abstractmethod
    def iter_relationships(self, **kwargs):
        """
        Iterate over `Relationship` instances. Derived classes will need to implement logic here
        to materialize data required and yield Relationship instances.

        """
