import sys
from functions import *

if __name__ == "__main__":
    print("PREDEFINED GRAPH")
    G = create_graph()

    s = G.V[0]
    dijkstra(G, s)

    for v in G.V:
        print("Path", s.val, "->", v.val, ":")
        print_path(G, s, v)
        print(v.d)
        print()

    print("RANDOM GENERATED GRAPH")
    G = generate_graph(5, 5, 10)
    s = G.V[0]

    print(G)

    dijkstra(G, s)

    for v in G.V:
        print("Path", s.val, "->", v.val, ":")
        print_path(G, s, v)
        print()
        print("Total distance: ", v.d)
    print()
