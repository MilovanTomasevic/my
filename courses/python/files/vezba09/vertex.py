import sys
from queue import Queue as queue

global time

class Vertex:
    def __init__(self, val):
        self.val = val
        self.con = []

    def print_neighbours(self):
        print([i.val for i in self.con])

    def add_neighbour(self, neighbour):
        self.con.append(neighbour)

class VertexColor:
    BLACK = 0
    GRAY = 127
    WHITE = 255
