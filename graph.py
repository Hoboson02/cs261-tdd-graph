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

    def adjacent (self, V1, V2): 
        if self._is_empty(): 
            return False
        v1List = self.neighbors(V1)
        if V2 in v1List: 
            return True 
    def _is_empty(self):
        if len(self.data) == 0: 
            return True 


    def neighbors(self, a): 
        if self._is_empty(): 
            return []
        if len(self.data) < 2: 
            return []
        return self.data.get(a, [])

    def add_vertex(self, newV): 
        for value in self.data: 
            if newV in self.data: 
                return
        self.data[newV] = []
        if self._is_empty() or self.data[newV] == 0 : 
            return None
        
        else: 
            add = self.data[newV]
            return add
        
    def remove_vertex(self, newV):
        if newV in self.data:
            self.remove_neighbors(newV)
            self.data.pop(newV)
        
    def add_edge(self, newE, newE2): 
        self.neighbors(newE).append(newE2)
        self.neighbors(newE2).append(newE)

    def remove_edge(self, newE, newE2): 
        if self._is_empty() or self.data[newE] == 0 and self.data[newE2] == 0: 
            return None
        
        else: 
            remove = self.data.pop(newE, newE2)
            return remove

    def remove_neighbors(self, value):
        for neighbor in self.neighbors(value): 
            if value in self.neighbors(neighbor): 
                self.neighbors(neighbor).remove(value)

    def add_neighbors(self, value):
        self.push(value)