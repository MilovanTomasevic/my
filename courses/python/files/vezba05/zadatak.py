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
