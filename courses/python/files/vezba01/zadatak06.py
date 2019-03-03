if __name__ == "__main__":
    l = []
    l.append((1, 2.3, "a"))
    l.append((4, 5.6, "abc"))
    l.append((7, 8.9, "ABC"))
    l.append((0, 1.2, "string"))
    print(l)
    l.remove(l[0])
    print(l)
