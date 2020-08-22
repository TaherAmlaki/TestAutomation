from typing import Dict, Set, List
from Visualizer.Tree import Node 


class FlattenGraph:
    def __init__(self, root: "Node"):
        self._visited_nodes = set()
        self.links = [{"child": root.name, "parent": ""}]
        self.extra_links = []
        self.leaf_nodes = []
        self._find_children(root)


    def _find_children(self, parent_node: "Node"):
        if len(parent_node.children) == 0:
            self.leaf_nodes.append(parent_node.name)
            
        for child in parent_node.children:
            if child.name not in self._visited_nodes:
                self._visited_nodes.add(child.name)
                self.links.append({"parent": parent_node.name, "child": child.name})
            else:
                self.extra_links.append({"parent": parent_node.name, "child": child.name})
            self._find_children(child)
    