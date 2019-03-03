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
