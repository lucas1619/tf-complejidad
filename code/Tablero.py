from listaenlazada import DoubleLinkedList
negro = (0, 0, 0)


class Tablero:
    def __init__(self, n):
        self.tam = 792/n
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

    def get_coord(self, value):
        coord = {"x": None, "y": None}
        coord['y'] = value//self.n
        coord['x'] = value % self.n
        return coord

    def graficar_tablero(self, pantalla, pygame):
        coord = None
        for i, _ in enumerate(self.grafo):
            coord = self.get_coord(i)
            pygame.draw.rect(
                pantalla, negro, (coord['x']*self.tam, coord['y']*self.tam, self.tam, self.tam), 1)

    def conectados(self, nodo1, nodo2):
        return nodo2 in self.grafo[nodo1]
    
    def eliminar_nodo(self, lista, nodo):
        self.grafo[lista].pop(nodo)

