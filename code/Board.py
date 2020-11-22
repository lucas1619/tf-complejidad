import networkx as nx
class Board:
    def __init__(self, size, G=None):
        self.size = size
        if G is None:
            self.G = nx.Graph()
            for i in range(size ** 2):
                self.G.add_node(i)
            for i in range(self.size ** 2):
                if i % self.size != self.size - 1:
                    self.G.add_edge(i, i + 1)
                    self.G.add_edge(i + 1, i)
                if i + self.size < self.size * self.size:
                    self.G.add_edge(i, i + self.size)
                    self.G.add_edge(i + self.size, i)
        else:
            self.G = G

    def copy(self):
        new_one = Board(self.size, self.G.copy())
        return new_one

    def add_wall(self, a1, b1, a2, b2, players):
        if ((self.size ** 2) > a1 >= 0) and ((self.size ** 2) > b1 >= 0) and ((self.size ** 2) > a2 >= 0) and (
                (self.size ** 2) > b2 >= 0):  # valida bordes
            pass
        else:
            return False  # valida bordes
        if self.G.has_edge(a1, a2) and self.G.has_edge(b1, b2) and self.G.has_edge(a1, b1) and self.G.has_edge(a2,
                                                                                                               b2):  # valida conexion entre nodos
            self.G.remove_edge(a1, b1)
            self.G.remove_edge(a2, b2)
        for player in players:
            if not player.path_find(self.G):
                self.G.add_edge(a1, b1)
                self.G.add_edge(b1, a1)
                self.G.add_edge(a2, b2)
                self.G.add_edge(b2, a2)
                return False
        return True