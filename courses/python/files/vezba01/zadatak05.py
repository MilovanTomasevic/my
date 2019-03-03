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
