---
layout: page
title: Z5-Rešenja
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
def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.data.a2)
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x == None or x.data.a1 == k:
        return x
    if k < x.data.a1:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x

def tree_successor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y

def tree_insert(T, z):
    y = None
    x = T
    while x != None:
        y = x
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T = z
    elif z.data.a1 < y.data.a1:
        y.left = z
    else:
        y.right = z
    return T

def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(tree_delete, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y

def transplant(T, u, v):
    if u.p == None:
        T = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p

def inorder_tree_walk_list(x, l):
    if x != None:
        inorder_tree_walk_list(x.left, l)
        l.append(x.data)
        inorder_tree_walk_list(x.right, l)
```
functions.py
{:.figure}

## Node

```py
class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self,  d = None, l = None, r = None):
        """
        Node constructor 
        @param A node data object
        """
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
```
node.py
{:.figure}

## Tree

```py
from functions import *

class Tree(object):
   
    def __init__(self, r = None):
        self.root = r

    def inorder_tree_walk(self):
        return inorder_tree_walk(self.root)

    def tree_search(self, k):
        return tree_search(self.root, k)

    def tree_minimum(self):
        return tree_minimum(self.root)

    def tree_maximum(self):
        return tree_maximum(self.root)

    def tree_successor(self, x):
        return tree_successor(x)

    def tree_insert(self, z):
        self.root = tree_insert(self.root, z)

    def tree_delete(self, z):
       return tree_delete(self.root, z)

    def transplant(self, u, v):
        transplant(self.root, u, v)

    def inorder_tree_walk_list(self, l):
            inorder_tree_walk_list(self.root, l)
```
tree.py
{:.figure}

## Zadatak 1

```py
import sys
from node import Data, Node
from tree import Tree
import random

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

if __name__ == "__main__":
    L = random_list(0, 10, 10)
    print(L)
    T = Tree()
    for i in L:
        d = Data(i, str(i))
        z = Node(d)
        T.tree_insert(z)

    print("\n--- inorder_tree_walk TEST ---")
    T.inorder_tree_walk()

    print("\n--- tree_search TEST ---")
    k = 8
    x = T.tree_search(k)
    print("Element" , k, "found" if x != None else "not found")
    k = 12
    x = T.tree_search(k)
    print("Element" , k, "found" if x != None else "not found")

    print("\n-- tree_successor TEST ---")
    k = 2
    x = T.tree_search(k)
    y = T.tree_successor(x)
    print("Successor(", x.data.a2, ") = ", y.data.a2)

    print("\n--- tree_minimum, tree_maximum TEST ---")
    min = T.tree_minimum()
    max = T.tree_maximum()
    print("min: ", min.data.a2, " max: ", max.data.a2)

    print ("\n--- delete(2) TEST ---")
    x = T.tree_search(2)
    T.tree_delete(x)
    T.inorder_tree_walk()
    
    print("\n--- inorder_tree_walk_list TEST ---")
    l = []
    T.inorder_tree_walk_list(l)
    print([x.a1 for x in l])
```
zadatak1.py
{:.figure}