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
        c = start % len(self.grafo)**0.5 + start // len(self.grafo)**0.5
        f = start // len(self.grafo)**0.5
        c1 = goal % len(self.grafo)**0.5 + goal // len(self.grafo)**0.5
        f1 = goal // len(self.grafo)**0.5
        grafoo = [Node_Astar(i) for i in range(len(self.grafo))]
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
                    c = neighbor % int(len(self.grafo) ** 0.5) + neighbor // int(len(self.grafo) ** 0.5)
                    f = neighbor // int(len(self.grafo) ** 0.5)
                    grafoo[neighbor].globhal = grafoo[neighbor].local + heuristic((c, f), (c1, f1))
        ruta.append(goal)
        ruta.pop(0)
        ruta.pop(0)
        return ruta

    def dijkstra(self, start, end):
        pass
