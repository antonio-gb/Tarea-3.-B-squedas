
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Grafo con costos
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3), ('G', 4)],
    'D': [('H', 3)],
    'E': [('H', 6)],
    'F': [('I', 4)],
    'G': [('J', 2)],
    'H': [('I', 1)],
    'I': [('J', 2)],
    'J': []
}

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]  # (g(n), nodo, camino)
    visited = {}
    while priority_queue:
        g, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path
        if node not in visited or g < visited[node]:
            visited[node] = g
            for neighbor, cost in graph.get(node, []):
                new_g = g + cost
                heapq.heappush(priority_queue, (new_g, neighbor, path + [neighbor]))
    return None

# Ejecutar la búsqueda
start, goal = 'A', 'J'
path_ucs = uniform_cost_search(graph, start, goal)
print("Camino encontrado por Uniform Cost Search:", path_ucs)

# Función para visualizar el grafo
def draw_graph(graph, path, title):
    G = nx.DiGraph()
    for node, neighbors in graph.items():
        for neighbor, _ in neighbors:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=12, font_weight="bold")
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

# Mostrar el grafo con el camino encontrado
draw_graph(graph, path_ucs, "Uniform Cost Search - Camino encontrado")

