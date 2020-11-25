import networkx as nx
import heapq as hp


def dijkstra(G, start, goal):
    return nx.dijkstra_path(G, start, goal)
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
                S.insert(0, nodo_distancia_minima)

                nodo_distancia_minima = anterior[nodo_distancia_minima]

            return S
    else:
         return S


def astar(G, start, goal):
    return nx.astar_path(G, start, goal)
    def heuristic(current, goal):
        h = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
        return float(h)

    def cercania(nodo1, nodo2):
        resta = nodo1 - nodo2
        lista = [-1, 1, size, -size]
        if resta in lista:
            return True

    inf = float("inf")
    tam_grafo = G.number_of_nodes()
    size = tam_grafo ** 0.5
    local = [inf] * tam_grafo
    visitado = [False] * tam_grafo
    local[start] = 0.0
    c = start % size + start // size
    f = start // size
    c1 = goal % size + goal // size
    f1 = goal // size
    current = start
    ruta = []
    q = [(heuristic((c, f), (c1, f1)), 0.0, False, start, start)]
    ruta.append(start)
    while len(q) and current != goal:

        g, l, v, current, papa = hp.heappop(q)
        if visitado[current]: continue
        if ruta.count(papa) == 0 and cercania(papa, ruta[-1]):
            ruta.append(papa)
        visitado[current] = True
        for neighbor in G.neighbors(current):
            sum = float(local[current] + 1)
            if (not visitado[neighbor]) and sum < local[neighbor]:
                local[neighbor] = sum
                c = neighbor % size + neighbor // size
                f = neighbor // size
                hp.heappush(q,
                            (local[neighbor] + heuristic((c, f), (c1, f1)), sum, visitado[neighbor], neighbor, current))
    if len(q) == 0 and current != goal:
        return []

    ruta.append(goal)
    return ruta


def bellman_ford(G, start, end):
    return nx.bellman_ford_path(G, start, end)
    distancias = dict()
    anterior = dict()
    for V in list(G):
        distancias[V] = float('Inf')
        anterior[V] = None
    distancias[start] = 0
    for V in list(G):
        for u, v in G.edges():
            distancia = distancias[u] + 1
            if distancia < distancias[v]:
                distancias[v] = distancia
                anterior[v] = u
    antes = anterior[end]
    path = [end]
    while antes != start and antes is not None:
        path.insert(0, antes)
        antes = anterior[antes]
    if antes == start:
        path.insert(0, start)
        return path
    return []
