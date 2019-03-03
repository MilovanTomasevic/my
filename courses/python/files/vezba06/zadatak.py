import sys
from math import inf


class histogram:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq

class node:
    def __init__(self, freq):
        self.freq = freq
        self.left = None
        self.right = None

def get_histogram(L):
    d = []
    res = []
    for i in L:
        if not i in d:
            d.append(i)
    for i in d:
        a = histogram(i, L.count(i))
        res.append(a)
    return res


def get_min_freq_elem(H):
    m = histogram('\0', inf)
    for i in H:
        if i.freq < m.freq:
            m = i
    return m


def remove_elem(el, L):
    L.remove(el)


def put_elem(el, L):
    L.append(el)


def make_new_elem(el1, el2):
    n = node(el1.freq + el2.freq)
    n.left = el1
    n.right = el2
    el1.par = n
    el2.par = n
    return n

def get_enc_val(ch, L):
    res = ""
    while not ch in L:
        if ch.par.left == ch:
            res += '0'
        elif ch.par.right == ch:
            res += '1'
        ch = ch.par
    return res[::-1]


def test(s):
    print(s)
    H = get_histogram(s)
    C = H[:]
    while len(H) > 1:
        m1 = get_min_freq_elem(H)
        remove_elem(m1, H)
        m2 = get_min_freq_elem(H)
        remove_elem(m2, H)
        m = make_new_elem(m1, m2)
        put_elem(m, H)
    for ch in C:
        print(ch.value, get_enc_val(ch, H))


if __name__ == "__main__":
    test_cases = [['a', 'b'], ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c'], ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd'], ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']]
    for s in test_cases:
        test(s)
