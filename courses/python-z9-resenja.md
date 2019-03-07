---
layout: page
title: Z9-Rešenja
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
from math import inf
from vertex import *

def bfs(G, s):
    for u in G:
        u.color = VertexColor.WHITE
        u.d = inf
        u.p = None
    s.color = VertexColor.GRAY
    s.d = 0
    s.p = None
    Q = queue()
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in u.con:
            if v.color == VertexColor.WHITE:
                v.color = VertexColor.GRAY
                v.d = u.d + 1
                v.p = u
                Q.put(v)
        u.color = VertexColor.BLACK

def print_path(G, s, v):
    if v == s:
        print(s.val, end = " ")
    elif v.p == None:
        print ("no path found from", s.val, "to", v.val, "exists")
    else:
        print_path(G, s, v.p)
        print(v.val, end = " ")

def dfs(G):
    global time
    for u in G:
        u.color = VertexColor.WHITE
        u.p = None
    time = 0
    for u in G:
        if u.color == VertexColor.WHITE:
            dfs_visit(G, u)

def dfs_visit(G, u):
    global time
    time += 1
    u.d = time
    u.color = VertexColor.GRAY

    for v in u.con:
        if v.color == VertexColor.WHITE:
            v.p = u
            dfs_visit(G, v)
    u.color = VertexColor.BLACK
    time += 1
    u.f = time

def topological_sort(G):
    dfs(G)
    L = sorted(G, key=lambda x: x.f, reverse=True)
    return L
```
functions.py
{:.figure}

## Vertex

```py
import sys
from queue import Queue as queue

global time

class Vertex:
    def __init__(self, val):
        self.val = val
        self.con = []

    def print_neighbours(self):
        print([i.val for i in self.con])

    def add_neighbour(self, neighbour):
        self.con.append(neighbour)

class VertexColor:
    BLACK = 0
    GRAY = 127
    WHITE = 255
```
vertex.py
{:.figure}

## Zadatak 1

```py
import sys
from functions import *

if __name__ == "__main__":
    print("\n===G1===")
    # Create graph 1
    G1 = []
    for i in range(5):
        g = Vertex(i + 1)
        G1.append(g)

    # Connect graph 1
    G1[0].add_neighbour(G1[1])
    G1[0].add_neighbour(G1[4])

    G1[1].add_neighbour(G1[0])
    G1[1].add_neighbour(G1[4])
    G1[1].add_neighbour(G1[2])
    G1[1].add_neighbour(G1[3])

    G1[2].add_neighbour(G1[1])
    G1[2].add_neighbour(G1[3])

    G1[3].add_neighbour(G1[1])
    G1[3].add_neighbour(G1[4])
    G1[3].add_neighbour(G1[2])

    G1[4].add_neighbour(G1[3])
    G1[4].add_neighbour(G1[0])
    G1[4].add_neighbour(G1[1])

    # Find neighbours of node 4
    print("Node 4 neighbours:")
    G1[3].print_neighbours()

    # Find path from node 4 to node 1
    print("Path 4->1")
    bfs(G1, G1[3])
    print_path(G1, G1[3], G1[0])

    print("\n===G2===")
    # Create nodes
    undershorts = Vertex("undershorts")
    pants = Vertex("pants")
    belt = Vertex("belt")
    shirt = Vertex("shirt")
    tie = Vertex("tie")
    jacket = Vertex("jacket")
    socks = Vertex("socks")
    shoes = Vertex("shoes")
    watch = Vertex("watch")

    # Create connections
    undershorts.con = [pants, shoes]
    pants.con = [belt, shoes]
    belt.con = [jacket]
    shirt.con = [tie, belt]
    tie.con = [jacket]
    jacket.con = []
    socks.con = [shoes]
    shoes.con = []
    watch.con = []

    # Create graph 2
    G2 = [shirt, undershorts, pants, belt, tie, jacket, socks, shoes, watch]

    # Topological sort
    L = topological_sort(G2)
    print([(i.val, i.d, i.f) for i in reversed(L)])
```
zadatak1.py
{:.figure}
