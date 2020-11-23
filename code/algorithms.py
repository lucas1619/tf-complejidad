import networkx as nx
def dijkstra(G, start, goal):

        grafo = nx.to_dict_of_lists(G)

        S = []
        Queue = []
        anterior = [0 for i in range(max(grafo) + 1)]
        distancia = [0 for i in range(max(grafo) + 1)]

        for nodo in grafo:
            distancia[nodo] = float("Inf")
            Queue.append(nodo)
        distancia[start] = 0

        while not len(Queue) == 0:
            distancia_minima = float("Inf")
            for nodo in Queue:
                if distancia[nodo] < distancia_minima:
                    distancia_minima = distancia[nodo]
                    nodo_temporal = nodo
            nodo_distancia_minima = nodo_temporal
            Queue.remove(nodo_distancia_minima)

            for vecino in grafo[nodo_distancia_minima]:
                if distancia[nodo_distancia_minima] == float("Inf"):
                    distancia_temporal = 0
                else:
                    distancia_temporal = distancia[nodo_distancia_minima]
                distancia_con_peso = distancia_temporal + 1
                if distancia_con_peso < distancia[vecino]:
                    distancia[vecino] = distancia_con_peso
                    anterior[vecino] = nodo_distancia_minima

            if nodo_distancia_minima == goal:
                if anterior[nodo_distancia_minima] != 0 or nodo_distancia_minima == start:

                    while nodo_distancia_minima != 0:

                        S.insert(0,nodo_distancia_minima)

                        nodo_distancia_minima = anterior[nodo_distancia_minima]

                    return S
def astar(G, origin, goal):
    return nx.astar_path(G, origin, goal)
def bellman_ford(G, origin, goal):
    return nx.bellman_ford_path(G, origin, goal)
