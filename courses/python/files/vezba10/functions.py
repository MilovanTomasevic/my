import sys
from graph import *
from math import inf
from random import randint

def create_graph():
    x = Vertex("x")
    y = Vertex("y")
    z = Vertex("z")
    s = Vertex("s")
    t = Vertex("t")

    V = [s, x, y, z, t]
    E = []

    E.append(Edge(s, y, 5))
    E.append(Edge(s, t, 10))

    E.append(Edge(y, t, 3))
    E.append(Edge(y, z, 2))
    E.append(Edge(y, x, 9))

    E.append(Edge(z, s, 7))
    E.append(Edge(z, x, 6))

    E.append(Edge(x, z, 4))

    E.append(Edge(t, x, 1))

    E.append(Edge(t, y, 2))

    return Graph(V, E)

def initialize_single_source(G, s):
    for v in G.V:
        v.d = inf
        v.p = None
    s.d = 0

def extract_min(V):
    m = V[0]
    for v in V:
        if v.d < m.d:
            m = v
    V.remove(m)
    return m

def relax(u, v, G):
    if v.d > u.d + G.get_edge_value(u, v):
        v.d = u.d + G.get_edge_value(u, v)
        v.p = u

def dijkstra(G, s):
    initialize_single_source(G, s)
    S = []
    Q = G.V[:]
    while Q:
        u = extract_min(Q)
        S.append(u)
        for v in G.get_neighbours(u):
            relax(u, v, G)

def print_path(G, s, v):
    if v == s:
        print(s.val, end=" ")
    elif v.p == None:
        print ("no path found from", s.val, "to", v.val, "exists")
    else:
        print_path(G, s, v.p)
        print(v.val, end=" ")

def generate_graph(n, m, edge):
    N = n
    G = Graph()
    for i in range(N):
        G.add_vertex(Vertex(i))

    for i in range(N):
        for j in range(randint(1, m)):
            r = i
            while r == i:
                r = randint(0, N - 1)
            G.add_edge(Edge(G.V[i], G.V[r], randint(0, edge)))
    return G
