import heapq as hp
import networkx as nx



def Astar(grafo, start, goal, size):

  def heuristic(current, goal):
    h = abs(current[0] - goal[0]) + abs(current[1] - goal[1])
    return float(h)

  inf = 10**18
  tam_grafo = size**2
  local = [inf] * tam_grafo
  visitado = [False] * tam_grafo
  local[start] = 0.0
  c = start % size + start //size
  f = start // size
  c1 = goal % size + goal // size
  f1 = goal // size
  current = start
  ruta = []
  q = [(heuristic((c, f), (c1, f1)), 0.0, False, start, start)]

  while len(q) and current!=goal :
    g, l, v, current, papa = hp.heappop(q)
    if visitado[current]: continue

    ruta.append(papa)
    
      
    visitado[current] = True

    for neighbor in grafo.neighbors(current):
       sum = float(local[current] + 1)

       if (not visitado[neighbor]) and sum < local[neighbor]:
         local[neighbor] = sum
         c = neighbor % size + neighbor // size
         f = neighbor // size
         hp.heappush(q, (local[neighbor] + heuristic((c, f), (c1, f1)), sum, visitado[neighbor], neighbor, current))

  ruta.append(goal), ruta.pop(0), ruta.pop(0)
  return ruta

G = nx.Graph()
size = 9
for i in range(size ** 2):
    G.add_node(i)
    for i in range(size ** 2):
        if i % size != size - 1:
            G.add_edge(i, i + 1)
            G.add_edge(i + 1, i)
        if i + size < size * size:
            G.add_edge(i, i + size)
            G.add_edge(i + size, i)

print(Astar(G,76,21,size))    