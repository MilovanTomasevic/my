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
