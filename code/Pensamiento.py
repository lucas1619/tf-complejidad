from listaenlazada import DoubleLinkedList
class Pensamiento:
    def __init__(self, Grafo, indica):
        self.grafo = Grafo
        self.indica = indica

    def actualiza_ruta(self, start, end):
        if self.indica == 1:
            return self.bellman_ford(start, end)
        elif self.indica == 2:
            return self.dijkstra(start, end)
        else:
            return self.astar(start, end)

    def bellman_ford(self, start, end):
        ruta = DoubleLinkedList()
        ruta.push_front(end)

        distancia = [float("Inf") for x in range(len(self.grafo))]

        previo = [-1 for x in range(len(self.grafo))]
        distancia[start] = 0
        for iteracion in range(len(self.grafo) - 1):
            for actual, nodo in enumerate(self.grafo):
                for adyacente in nodo:
                    if distancia[actual] + 1 < distancia[adyacente]:
                        distancia[adyacente] = distancia[actual] + 1
                        previo[adyacente] = actual
        anterior = previo[end]
        while anterior != start:
            ruta.push_front(anterior)
            anterior = previo[anterior]
        return list(ruta)

    def astar(self, start, end):
        pass

    def dijkstra(self, start, end):
        pass
