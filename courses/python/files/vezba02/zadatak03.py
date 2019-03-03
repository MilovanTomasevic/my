import random
import time

def random_list(min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

def test(elements):
    l = list(set(random_list(1, elements + 1, elements)))
    start_time = time.clock()

    ind = linear_search(l, random.randint(1, elements))

    end_time = time.clock() - start_time
    print("Elements:", elements, "Index:", ind, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(5000, 50000, 5000):
        test(i)
