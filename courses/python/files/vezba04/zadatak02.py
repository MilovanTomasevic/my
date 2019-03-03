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
