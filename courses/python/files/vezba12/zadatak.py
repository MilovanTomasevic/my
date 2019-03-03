import sys
import random
import time


def random_list(values, elements):
    list = [random.choice(values) for _ in range(elements)]
    return list

def lcs(S, n, T, m):
    if n < 0 or m < 0:
        return 0
    if S[n] == T[m]:
        return 1 + lcs(S, n - 1, T, m - 1)
    else:
        return max(lcs(S, n - 1, T, m), lcs(S, n, T, m - 1))

def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for i in range(n)] for j in range(m)]
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m):
        for j in range(n):
            I = i + 1
            J = j + 1
            if X[i] == Y[j]:
                c[I][J] = c[I - 1][J - 1] + 1
                b[i][j] = Direction.UPLEFT
            elif c[I - 1][J] >= c[I][J - 1]:
                c[I][J] = c[I - 1][J - 1]
                b[i][j] = Direction.UP
            else:
                c[I][J] = c[I][J - 1]
                b[i][j] = Direction.LEFT
    return (c, b)

def print_lcs(b, X, i, j):
    if i < 0 or j < 0:
        return
    if b[i][j] == Direction.UPLEFT:
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end="")
    elif b[i][j] == Direction.UP:
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

class Direction:
    UP = "↑"
    LEFT = "←"
    UPLEFT = "↖"

def test_dynamic(i):
    l1 = random_list("ABCDEFGHIJKLMNOPQRSTUVWXZ", i)
    l2 = random_list("ABCDEFGHIJKLMNOPQRSTUVWXZ", i)

    start_time = time.clock()

    (c, b) = lcs_length(l1, l2)

    end_time = time.clock() - start_time

    print("Elements:", i, "Duration dynamic: ", end_time)

def test_iterative(i):
    l1 = random_list("ABCDEFGHIJKLMNOPQRSTUVWXZ", i)
    l2 = random_list("ABCDEFGHIJKLMNOPQRSTUVWXZ", i)

    start_time = time.clock()

    lcs(l1, len(l1) - 1, l2, len(l2) - 1)

    end_time = time.clock() - start_time

    print("Elements:", i, "Duration iterative: ", end_time)


if __name__ == "__main__":
    X = "BDCABA"
    Y = "ABCBDAB"
    print("X =", X)
    print("Y =", Y)
    n = lcs(X, len(X) - 1, Y, len(Y) - 1)
    print(n)

    (c, b) = lcs_length(X, Y)

    print_lcs(b, X, len(X) - 1, len(Y) - 1)
    print()

    # Test speed
    for i in [10, 50, 100, 500, 1000, 5000]:
        test_dynamic(i)

    for i in [5, 10, 11, 12, 13, 14, 15]:
        test_iterative(i)
