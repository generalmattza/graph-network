#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Matthew Davidson
# Created Date: 2023-01-23
# version ='1.0'
# ---------------------------------------------------------------------------
"""A simple edge class, which can be used for deriving new edge classes that
actually do something useful"""
# ---------------------------------------------------------------------------

from __future__ import annotations
from typing import TYPE_CHECKING

from src.id_generator import IDGenerator

if TYPE_CHECKING:
    from node import Node


class Edge:
    _ids: IDGenerator = IDGenerator()

    def __init__(self, id: str = None, name: str = "path", nodes: set = None):
        if id is None:
            id = Edge._ids.get_new_id()
        self.name: str = f"{name}{id}"
        if nodes is None:
            self.nodes: set[Node, Node] = set()
        else:
            self.nodes = set(nodes)

    def __repr__(self):
        return str(self.name)

    def get_nodes(self) -> set:
        sort = lambda node: node.target_key
        return sorted(set(self.nodes), key=sort)

    def add_node(self, node: Node) -> None:
        if node not in self.nodes:
            self.nodes.add(node)
