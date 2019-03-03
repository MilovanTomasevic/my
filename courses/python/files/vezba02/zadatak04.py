import random
import time

def generate_list(min, max):
    list = [x for x in range(min, max)] 
    return list

def binary_search(arr, val, left, right):
    i = int((left + right) / 2)
    if arr[i] == val:
        return i
    elif left >= right or i == left or i == right:
        return -1
    elif arr[i] > val:
        return binary_search(arr, val, left, i)
    else:
        return binary_search(arr, val, i, right)

def test(elements):
    l = generate_list(1, elements)
    start_time = time.clock()

    ind = binary_search(l, random.randint(1, elements), 0, len(l))

    end_time = time.clock() - start_time
    print("Elements:", elements, "Index:", ind, "Duration: ", end_time)

if __name__ == "__main__":
    for i in range(10000, 500000, 10000):
        test(i)
