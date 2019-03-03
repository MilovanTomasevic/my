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
