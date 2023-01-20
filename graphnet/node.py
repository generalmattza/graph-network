from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from graphnet.id_generator import IDGenerator
from typing import TYPE_CHECKING, Container

if TYPE_CHECKING:
    from graphnet.edge import Edge


@dataclass
class NodePlot:
    xy: tuple


class Node(ABC):
    _ids: IDGenerator = IDGenerator()

    def __init__(
        self,
        id: str = None,
        name: str = "Node",
        plot: dict = None,
        edges: Container[Edge] = None,
    ):
        if id is None:
            id = Node._ids.get_new_id()
            self.id: str = f"{name}{id}"
        else:
            self.id = id
        if plot is not None:
            self.plot: NodePlot = NodePlot(**plot)

        if edges is not None:
            self.edges = set(edges)
        else:
            self.edges: set = set()

    def add_edge(self, edge: Edge, target: Node) -> None:
        self.edges.add(edge)
        edge.add_node(self)
        edge.add_node(target)

    def __repr__(self) -> str:
        return str(self.id)
