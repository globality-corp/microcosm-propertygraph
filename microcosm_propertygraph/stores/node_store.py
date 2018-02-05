"""
Node persistence.

"""
from abc import ABCMeta, abstractmethod
from itertools import islice

from microcosm.api import binding
from microcosm_postgres.store import Store

from microcosm_propertgraph.models.node import Node


@binding("node_store")
class NodeStore(Store, metaclass=ABCMeta):

    def __init__(self, graph, model_class=Node):
        super(NodeStore, self).__init__(graph, model_class)

    def count(self, **kwargs):
        return sum(1 for n in self.iter_nodes(**kwargs))

    def search(self, offset, limit, **kwargs):
        return islice(
            self.iter_nodes(**kwargs),
            offset,
            limit,
        )

    @abstractmethod
    def iter_nodes(self, **kwargs):
        """
        Iterate over `Node` instances. Derived classes will need to implement logic here
        to materialize data required and yield Node instances.

        """
