---
layout: page
title: Z11-Rešenja
description: >
  Python is an easy to learn, powerful programming language. ... experience, but all examples are self-contained, so the tutorial can be read off-line as well.
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Functions

```py
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
```
functions.py
{:.figure}

## Graph

```py
import sys
from math import inf

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

    def update_edge_value(self, u, v, val):
        for i in self.E:
            if i.first == u and i.second == v:
                i.val = val

    def __str__(self):
        return "Nodes: " + str([f"{i.val}" for i in self.V]) + "\nConnections: " + str([f"({i.first.val}, {i.second.val}, {i.val})" for i in self.E])
```
graph.py
{:.figure}

## Zadatak 1

```py
import sys
from functions import *

if __name__ == "__main__":
    # Zadatak 1
    print ("\nZadatak 1 - MakeGraph()")
    G = make_graph()
    print([x.val for x in G.V])
    print([(x.first.val, x.second.val, x.val) for x in G.E])

    # Zadatak 2
    print ("\nZadatak 2 - GetInDegrees(), GetOutDegrees()")
    Lin = get_in_degrees(G)
    Lout = get_out_degrees(G)

    for i in range(len(G.V)):
        print("Node:", G.V[i].val, "In degrees:", Lin[i], "Out degrees:", Lout[i])

    # Zadatak 3
    print ("\nZadatak 3 - ShortestPath()")
    bellman_ford(G, G.V[0])
    (L, n) = shortest_path(G, G.V[0], G.V[6])

    print("Shortest path from", G.V[0].val, "to", G.V[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()

    # Zadatak 4
    print("\nZadatak 4 - UpdateEdge()")
    update_edge(G, G.V[0], G.V[1], 8)
    update_edge(G, G.V[1], G.V[2], -6)
    print([(x.first.val, x.second.val, x.val) for x in G.E])

    # Zadatak 5
    print("\nZadatak 5")
    bellman_ford(G, G.V[0])
    (L, n) = shortest_path(G, G.V[0], G.V[6])

    print("New shortest path from", G.V[0].val, "to", G.V[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()
```
zadatak1.py
{:.figure}