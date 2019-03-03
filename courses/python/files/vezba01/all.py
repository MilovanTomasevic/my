



#primer01.py

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




#zadatak01.py

def zbir(n):
    if n <= 0:
        return 0
    else:
        return n + zbir(n - 1)

if __name__ == "__main__":
    print(zbir(eval(input())))


#zadatak02.py


#zadatak03.py


#zadatak04.py


#zadatak05.py

#zadatak06.py

#zadatak07.py


