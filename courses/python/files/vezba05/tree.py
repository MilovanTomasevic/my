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
