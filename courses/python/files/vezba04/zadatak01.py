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
