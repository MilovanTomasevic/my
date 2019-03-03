import sys
import random
import time
from math import inf
from math import floor

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []
    i, j = 0, 0
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def test(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()
    
    merge_sort(l, 0, len(l) - 1)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test(i)
