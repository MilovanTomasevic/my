import sys

class Vertex:
    def __init__(self, val):
        self.val = val

class Edge:
    def __init__(self, u, v, val):
        self.first = u
        self.second = v
        self.val = val

class Graph:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E

    def add_vertex(self, v):
        self.V.append(v)

    def add_edge(self, edge):
        self.E.append(edge)

    def get_neighbours(self, v):
        L = []
        for i in self.E:
            if i.first == v:
                L.append(i.second)
        return L

    def get_edge_value(self, u, v):
        for i in self.E:
            if i.first == u and i.second == v:
                return i.val
        return inf

    def __str__(self):
        return "Nodes: " + str([f"{i.val}" for i in self.V]) + "\nConnections: " + str([f"({i.first.val}, {i.second.val}, {i.val})" for i in self.E])
