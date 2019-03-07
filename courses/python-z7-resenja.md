---
layout: page
title: Z7-Rešenja
description: >
  Python is an easy to learn, powerful programming language. ... experience, but all examples are self-contained, so the tutorial can be read off-line as well.
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Zadatak 1

```py
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

```
zadatak1.py
{:.figure}

## Zadatak 2

```py
import math
import random
import time
from math import floor

class Data:
    def __init__(self, key=None):
        self.key = key
        self.literal = str(key)

class HashTable:
    def __init__(self, m=10000, c1=1/2, c2=1/2):
        self.m = m
        self.c1 = c1
        self.c2 = c2
        self.T = [None] * m

    def insert(self, k):
        i = 0
        while True:
            j = self.hash(k, i)
            if self.T[j] == None:
                self.T[j] == k
                return j
            else:
                i += 1
            if i == self.m:
                break
        print("ERROR 408")

    def search(self, k):
        i = 0
        while True:
            j = self.hash(k, i)
            if self.T[j] == None:
                return j
            i += 1
            if self.T[j] == None or i == self.m:
                break
        return None

    def delete(self, x):
        h = self.hash(x.key)
        if x in self.L[h]:
            self.L[h].remove(x)

    def h1(self, k):
        return k % self.m

    def h2(self, k):
        return 1 + (k % (self.m - 1))

    def hash1(self, k, i):
        return (self.h1(k) + i) % self.m

    def hash2(self, k, i):
        return (self.h1(k) + self.c1*i + self.c2*i**2) % self.m

    def hash3(self, k, i):
        return (self.h1(k) + self.h2(k)) % self.m

    def hash(self, k, i):
        return self.hash1(k, i)

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def test(n, m):
    l = random_list(1, n + 1, n)
    start_time = time.clock()

    L = HashTable(m)

    for i in l:
        L.insert(i)

    end_time = time.clock() - start_time

    print("n:", n, "m:", m, "duration:", end_time)

if __name__ == "__main__":
    for n in [10000, 50000, 100000]:
        for m in [n, n//2, n//4]:
            test(n, m)
```
zadatak2.py
{:.figure}