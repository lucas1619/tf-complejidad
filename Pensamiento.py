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

        distancia = [float("Inf") for x in range(self.grafo.q_nodos)]

        previo = [-1 for x in range(self.grafo.q_nodos)]
        distancia[start] = 0
        for iteracion in range(self.grafo.q_nodos - 1):
            for actual, nodo in enumerate(self.grafo):
                for adyacente in nodo:
                    if distancia[actual] + 1 < distancia[adyacente]:
                        distancia[adyacente] = distancia[actual] + 1
                        previo[adyacente] = actual
        anterior = previo[end]
        while anterior != -1:
            ruta.push_front(anterior)
            anterior = previo[anterior]
        return list(ruta)

    def astar(self, start, end):
        pass

    def dijkstra(self, start, end):
        pass
