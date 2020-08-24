from enum import Enum, auto 
from typing import List  


class NodeTypes(Enum):
    SUITE = auto()
    TEST_CASE = auto()
    KEYWORD = auto()


class Node:
    def __init__(self, name: str, node_type: NodeTypes = NodeTypes.KEYWORD):
        self.parent : "Node" = None
        self.children: List["Node"] = []
        self.name = name 
        self.node_type = node_type
    
    def add_child(self, child: "Node"):
        child.parent = self
        self.children.append(child)
    
    def to_hierarchical(self):
        children = [child.to_hierarchical() for child in self.children]
        d = {"name": self.name}
        if 0 < len(children):
            d['children'] = children 
        return d
    
    def __str__(self):
        return self.name 


    