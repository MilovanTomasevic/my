import sys
from functions import *

if __name__ == "__main__":
    # Zadatak 1
    print ("\nZadatak 1 - MakeGraph()")
    G = make_graph()
    print([x.val for x in G.V])
    print([(x.first.val, x.second.val, x.val) for x in G.E])

    # Zadatak 2
    print ("\nZadatak 2 - GetInDegrees(), GetOutDegrees()")
    Lin = get_in_degrees(G)
    Lout = get_out_degrees(G)

    for i in range(len(G.V)):
        print("Node:", G.V[i].val, "In degrees:", Lin[i], "Out degrees:", Lout[i])

    # Zadatak 3
    print ("\nZadatak 3 - ShortestPath()")
    bellman_ford(G, G.V[0])
    (L, n) = shortest_path(G, G.V[0], G.V[6])

    print("Shortest path from", G.V[0].val, "to", G.V[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()

    # Zadatak 4
    print("\nZadatak 4 - UpdateEdge()")
    update_edge(G, G.V[0], G.V[1], 8)
    update_edge(G, G.V[1], G.V[2], -6)
    print([(x.first.val, x.second.val, x.val) for x in G.E])

    # Zadatak 5
    print("\nZadatak 5")
    bellman_ford(G, G.V[0])
    (L, n) = shortest_path(G, G.V[0], G.V[6])

    print("New shortest path from", G.V[0].val, "to", G.V[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()

