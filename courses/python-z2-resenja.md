---
layout: page
title: Z2-Rešenja
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
```
zadatak1.py
{:.figure}

## Zadatak 2

```py
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
```
zadatak2.py
{:.figure}

## Zadatak 3

```py
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
```
zadatak3.py
{:.figure}

## Zadatak 4

```py
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
```
zadatak4.py
{:.figure}