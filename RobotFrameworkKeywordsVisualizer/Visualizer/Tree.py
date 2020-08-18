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
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level 
    
    def print_tree(self):
        prefix = "\t" * self.get_level() + "|-- " if self.parent else "=> "
        print(prefix + self.name)
        for child in self.children:
            child.print_tree()