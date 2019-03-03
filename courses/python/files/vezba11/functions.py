import sys
from graph import *
from math import inf

def make_graph():
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")

    vertex = [a, b, c, d, e, f, g]

    edges = []

    edges.append(Edge(a, b, 8))
    edges.append(Edge(a, c, 6))
    edges.append(Edge(b, d, 10))
    edges.append(Edge(c, e, 9))
    edges.append(Edge(c, d, 15))
    edges.append(Edge(d, e, 14))
    edges.append(Edge(d, f, 4))
    edges.append(Edge(e, f, 13))
    edges.append(Edge(e, g, 17))
    edges.append(Edge(f, g, 7))

    return Graph(vertex, edges)

def initialize_single_source(G, s):
    for v in G.V:
        v.d = inf
        v.p = None
    s.d = 0

def relax(u, v, G):
    if v.d > u.d + G.get_edge_value(u, v):
        v.d = u.d + G.get_edge_value(u, v)
        v.p = u

def bellman_ford(G, s):
    initialize_single_source(G, s)
    for i in range(len(G.V)):
        for edge in G.E:
            relax(edge.first, edge.second, G)
    for edge in G.E:
        if edge.first.d > edge.second.d + G.get_edge_value(edge.first, edge.second):
            return False
    return True

def get_in_degrees(G):
    L = []
    for v in G.V:
        n = 0
        for edge in G.E:
            if edge.second == v:
                n += 1
        L.append(n)
    return L

def get_out_degrees(G):
    L = []
    for v in G.V:
        n = 0
        for edge in G.E:
            if edge.first == v:
                n += 1
        L.append(n)
    return L

def shortest_path(G, nodeA, nodeB):
    bellman_ford(G, nodeA)
    L = []
    L = create_path(G, nodeA, nodeB, L)
    n = G.V[-1].d
    return (L, n)

def create_path(G, s, v, L):
    if v == s:
        L.append(v)
    elif v.p == None:
        return None
    else:
        create_path(G, s, v.p, L)
        L.append(v)
    return L

def update_edge(G, nodeA, nodeB, weight):
    if G.get_edge_value(nodeA, nodeB) != inf:
        G.update_edge_value(nodeA, nodeB, weight)
    else:
        G.add_edge(Edge(nodeA, nodeB, weight))
