from listaenlazada import DoubleLinkedList


class Tablero:
    def init(self, n):
        self.n = n
        self.q_nodos = n * n
        self.grafo = [DoubleLinkedList() for i in range(self.q_nodos)]
        for i, nodo in enumerate(self.grafo):
            if i % n != n - 1:
                self.grafo[i].push_back(i + 1)
                self.grafo[i + 1].push_back(i)
            if i + n < n * n:
                self.grafo[i].push_back(i + n)
                self.grafo[i + n].push_back(i)


