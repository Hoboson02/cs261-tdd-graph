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
        
    def remove_vertex (self, newV): 
        if self._is_empty() or self.data[newV] == 0: 
            return None
        
        else: 
            remove = self.data.pop()
            return remove
        
    def add_edge(self, newE, newE2): 
        if self._is_empty() or self.data[newE] == 0 and self.data[newE2] == 0: 
            return None
        
        else: 
            add = self.data.append() 
            return add

    def remove_edge(self, newE, newE2): 
        if self._is_empty() or self.data[newE] == 0 and self.data[newE2] == 0: 
            return None
        
        else: 
            remove = self.data.pop()
            return remove