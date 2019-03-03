import sys
import random
import time

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

def test(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()
    
    quicksort(l, 0, len(l) - 1)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 10000, 500):
        test(i)
