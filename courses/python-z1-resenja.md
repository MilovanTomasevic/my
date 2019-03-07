---
layout: page
title: Z1-Rešenja
description: >
  Python is an easy to learn, powerful programming language. ... experience, but all examples are self-contained, so the tutorial can be read off-line as well.
hide_description: true

---

## Table of Contents
{:.no_toc}
0. this unordered seed list will be replaced by toc as unordered list
{:toc}

---

## Primer 1

```py
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error")
        sys.exit()
    key = sys.argv[1]
    val = [(i, i + 1) for i in range(0, 10, 2)]
    d = {}
    d[key] = val
    print(d)
```
primer1.py
{:.figure}

## Zadatak 1

```py
def zbir(n):
    if n <= 0:
        return 0
    else:
        return n + zbir(n - 1)

if __name__ == "__main__":
    print(zbir(eval(input())))

```
zadatak1.py
{:.figure}

## Zadatak 2

```py
import sys

def kv_zbir(n):
    if n <= 0:
        return 0
    else:
        return n**2 + kv_zbir(n - 1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error")
        sys.exit()
    n = int(sys.argv[1])
    print(kv_zbir(n))
```
zadatak2.py
{:.figure}

## Zadatak 3

```py
if __name__ == "__main__":
    str1 = input()
    str2 = input()
    str3 = str1[:3] * 2 + str2[-3:];
    print(str3)
```
zadatak3.py
{:.figure}

## Zadatak 4

```py
if __name__ == "__main__":
    l = [i + 1 for i in range(100)]
    print (l[::-1])
```
zadatak4.py
{:.figure}

## Zadatak 5

```py
if __name__ == "__main__":
    f = open("dict_test.txt", "r")
    d = dict()
    for line in f:
        words = line.split()
        for word in words:
            if not word in d:
                d[word] = 1
            else:
                d[word] += 1
    for key, value in d.items():
        print(key, ":", value)
    f.close()
```
zadatak5.py
{:.figure}

## Zadatak 6

```py
if __name__ == "__main__":
    l = []
    l.append((1, 2.3, "a"))
    l.append((4, 5.6, "abc"))
    l.append((7, 8.9, "ABC"))
    l.append((0, 1.2, "string"))
    print(l)
    l.remove(l[0])
    print(l)
```
zadatak6.py
{:.figure}

## Zadatak 7

```py
if __name__ == "__main__":
    s = set()
    el0 = 1, 2.3, "a"
    el1 = 4, 5.6, "abc"
    el2 = 7, 8.9, "ABC"
    el3 = 0, 1.2, "string"
    s.add(el0)
    s.add(el1)
    s.add(el2)
    s.add(el3)
    print(s)
    s.remove(el0)
    print(s)
```
zadatak7.py
{:.figure}
