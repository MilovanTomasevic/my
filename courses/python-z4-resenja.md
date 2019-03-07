---
layout: page
title: Z4-Rešenja
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
import sys
import random
import time

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def parent(i):
    return i // 2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(A, i, size):
    l = left(i)
    r = right(i)
    if l < size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, size)

def build_max_heap(A):
    size = len(A)
    for i in reversed(range(len(A) - 1)):
        max_heapify(A, i, size)

def heap_sort(A):
    size = len(A)
    build_max_heap(A)
    for i in reversed(range(1, size)):
        A[0], A[i] = A[i], A[0]
        size -= 1
        max_heapify(A, 0, size);

def test(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()
    
    heap_sort(l)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test(i)
```
zadatak1.py
{:.figure}

## Zadatak 2

```py
import sys
import random
import time

def random_list(min, max, elements):
    list = [random.choice(range(min, max)) for _ in range(elements)]
    return list

def index(i):
    return i // 100

def bucket_sort(A):
    size = 10
    B = [0] * (size)
    for i in range(size - 1):
        B[i] = []
    for i in range(len(A)):
        B[index(A[i])].append(A[i])
    for i in range(0, size-1):
        B[i].sort()
    A.clear()
    for i in range(size - 1):
        A += B[i]

def test(elements):
    l = random_list(0, 100, elements)
    start_time = time.clock()
    
    bucket_sort(l)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test(i)
```
zadatak2.py
{:.figure}

## Zadatak 3

```py
import sys
import random
import time

def random_list(min, max, elements):
    list = [random.choice(range(min, max)) for _ in range(elements)]
    return list

def counting_sort(A, B, k):
    C = [0] * k
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    
    
    for j in reversed(range(len(A))):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

def test(elements):
    l = random_list(0, 100, elements)
    r = [0] * len(l)
    k = max(l) + 1
    start_time = time.clock()
    
    counting_sort(l, r, k)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test(i)
```
zadatak3.py
{:.figure}