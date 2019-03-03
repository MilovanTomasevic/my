def zbir(n):
    if n <= 0:
        return 0
    else:
        return n + zbir(n - 1)

if __name__ == "__main__":
    print(zbir(eval(input())))
