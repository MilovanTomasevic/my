import math
import random
import time
from math import floor

class Data:
    def __init__(self, key=None):
        self.key = key
        self.literal = str(key)

class ChainedHash:
    def __init__(self, p = 27, m = 10000):
        self.p = p
        self.m = m
        self.a = random.randint(0, p)
        self.b = random.randint(1, p)
        self.L = [[]] * m

    def insert(self, x):
        h = self.hash(x.key)
        if x in self.L[h]:
            self.L[h].remove(x)
        self.L[h].append(x)

    def search(self, k):
        h = self.hash(k)
        for i in self.L[h]:
            if i.key == k:
                return i
        return None

    def delete(self, x):
        h = self.hash(x.key)
        if x in self.L[h]:
            self.L[h].remove(x)

    def hash1(self, k):
        return k % m

    def hash2(self, k):
        KNUTH = 0.6180339887
        return floor(m * ((k * KNUTH) % 1))

    def hash3(self, k):
        return ((a*k + b) % p) % m

    def hash(self, k):
        return self.hash1(k)

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list


def test(n, p, m):
    l = random_list(1, n + 1, n)
    start_time = time.clock()

    L = ChainedHash(p, m)

    for i in l:
        x = Data(i)
        L.insert(x)

    end_time = time.clock() - start_time


    print("n:", n, "m:", m, "p:", p, "duration:", end_time)

if __name__ == "__main__":
    for n in [10000, 50000, 100000]:
        for p in [23, 9973, 99991]:
            for m in [p, p//2, p//4]:
                test(n, p, m)
