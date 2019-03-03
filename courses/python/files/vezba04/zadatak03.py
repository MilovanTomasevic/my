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
