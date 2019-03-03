import random
import time

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

def test(elements):
    l = random_list(1, elements + 1, elements)
    start_time = time.clock()

    insertion_sort(l)

    end_time = time.clock() - start_time
    print("Elements:", elements, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(500, 5000, 500):
        test(i)
