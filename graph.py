# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices
# and edges.
# Your implementation should pass the tests in test_graph.py.
# Ryan Earl

import functools

class Graph:

    def __init__ (self): 
        self.data = {}
        return None
    pass

    def adjacent (self, aVertices, bVertices): 
        return None
    
    def _is_empty(self):
        if len(self.data) == 0: 
            return True 


    def neighbors(self, a): 
        if self._is_empty(): 
            return []

    def add_vertex(self, newV): 
        self.data[newV] = []