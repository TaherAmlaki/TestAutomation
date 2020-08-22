from copy import deepcopy
from Visualizer.Tree import NodeTypes, Node 


class VisualizerListener:
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, max_level: int = None, ignore_builtin: bool = True):
        self.max_level = max_level
        self.ignore_builtin = ignore_builtin
        self._current_level = 0
        self._stack = []
        self._root = None
        self.trees = []

    def start_suite(self, name, attributes):
        self._root = Node(name, NodeTypes.SUITE)
        self._stack = [self._root]

    def start_test(self, name, attributes):
        test_node = Node(name, NodeTypes.TEST_CASE)
        self._root.add_child(test_node) 
        self._stack.append(self._root.children[-1])

    def start_keyword(self, name: str, attributes):
        self._current_level += 1
        if self.max_level is None or self._current_level < self.max_level:
            if self.ignore_builtin and not name.startswith("BuiltIn"):
                keyword_node = Node(name, NodeTypes.KEYWORD)
                self._stack[-1].add_child(keyword_node)
                self._stack.append(self._stack[-1].children[-1]) 

    def end_keyword(self, name, attributes):
        if self.max_level is None or self._current_level < self.max_level:
            if self.ignore_builtin and not name.startswith("BuiltIn"):
                self._stack.pop()
        self._current_level -= 1

    def end_test(self, name, attributes):
        self._stack.pop()

    def end_suite(self, name, attributes):
        self._stack.pop()
        self.trees.append(deepcopy(self._root))
        self.root = None 
        