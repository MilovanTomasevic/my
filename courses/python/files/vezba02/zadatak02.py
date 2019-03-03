import random
import time

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t

def test(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()
    
    bubble_sort(l)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 5000, 500):
        test(i)
