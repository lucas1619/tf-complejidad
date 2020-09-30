from listaenlazada import DoubleLinkedList


class Node_Astar:
    def __init__(self, pos, padre=None, local=float("inf"), globhal=float("inf"), visited=False):
        self.pos = pos
        self.padre = padre
        self.local = local
        self.globhal = globhal
        self.visited = visited

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

    def astar(self, start, goal):  # self.n

        def heuristic(current, goal):
            h = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
            return float(h)

        def get_heuristic_value(node):
            return node.globhal

        current = start
        c = start % self.grafo.n + start // self.grafo.n
        f = start // self.grafo.n
        c1 = goal % self.grafo.n + goal // self.grafo.n
        f1 = goal // self.grafo.n
        grafoo = [Node_Astar(i) for i in range(self.grafo.n * self.grafo.n)]
        grafoo[start].local = 0.0
        grafoo[start].globhal = heuristic((c, f), (c1, f1))
        not_tested_nodes = [grafoo[start]]
        ruta = []

        while len(not_tested_nodes) != 0 and current != goal:

            not_tested_nodes.sort(key=get_heuristic_value)

            while len(not_tested_nodes) != 0 and not_tested_nodes[0].visited:
                not_tested_nodes.pop(0)

            if len(not_tested_nodes) == 0:
                break

            current = not_tested_nodes[0].pos
            ruta.append(grafoo[current].padre)
            not_tested_nodes[0].visited = True

            for neighbor in self.grafo[current]:

                if not grafoo[neighbor].visited:
                    not_tested_nodes.append(grafoo[neighbor])

                sum = float(grafoo[current].local + 1)

                if sum < grafoo[neighbor].local:
                    grafoo[neighbor].padre = current
                    grafoo[neighbor].local = sum
                    c = neighbor % self.grafo.n + neighbor // self.grafo.n
                    f = neighbor // self.grafo.n
                    grafoo[neighbor].globhal = grafoo[neighbor].local + \
                        heuristic((c, f), (c1, f1))

        ruta.append(goal)
        ruta.pop(0)
        return ruta

    def dijkstra(self, start, end):
        pass
