from listaenlazada import DoubleLinkedList


class Node_Astar:
    def __init__(self, pos, padre=None, local=float("inf"), globhal=float("inf"), visited=False):
        self.pos = pos
        self.padre = padre
        self.local = local
        self.globhal = globhal
        self.visited = visited


# crear el grafo
class Quoridor:
    def __init__(self, n=3, q_players=2):
        self.n = n
        self.q_nodos = n * n
        self.q_players = 2
        self.grafo = [DoubleLinkedList() for i in range(self.q_nodos)]
        for i, nodo in enumerate(self.grafo):
            if i % n != n - 1:
                self.grafo[i].push_back(i + 1)
                self.grafo[i + 1].push_back(i)
            if i + n < self.q_nodos:
                self.grafo[i].push_back(i + n)
                self.grafo[i + n].push_back(i)

    def bellman_ford(self, start, end):

        ruta = DoubleLinkedList()
        ruta.push_front(end)
        distancia = [float("Inf") for x in range(self.q_nodos)]
        previo = [-1 for x in range(self.q_nodos)]
        distancia[start] = 0
        for iteracion in range(self.q_nodos - 1):
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


    def Astar(self, start, goal):  # self.n

        def heuristic(current, goal):
            h = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
            return float(h)

        def get_heuristic_value(node):
            return node.globhal

        current = start
        c = start % self.n + start // self.n
        f = start // self.n
        c1 = goal % self.n + goal // self.n
        f1 = goal // self.n
        grafoo = [Node_Astar(i) for i in range(self.n * self.n)]
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
                    c = neighbor % self.n + neighbor // self.n
                    f = neighbor // self.n
                    grafoo[neighbor].globhal = grafoo[neighbor].local + heuristic((c, f), (c1, f1))

        ruta.append(goal)
        ruta.pop(0)
        return ruta



juego = Quoridor(9)
print(juego.bellman_ford(0, 44))
print(juego.Astar(0, 44))