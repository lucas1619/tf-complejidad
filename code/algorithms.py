import networkx as nx
def dijkstra(G, origin, goal):
    return nx.dijkstra_path(G, origin, goal)
def astar(G, origin, goal):
    return nx.astar_path(G, origin, goal)
def bellman_ford(G, origin, goal):
    return nx.bellman_ford_path(G, origin, goal)