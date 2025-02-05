import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Grafo con costos y heurística
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

heuristic = {
    'A': 7,
    'B': 6,
    'C': 3,
    'D': 5,
    'E': 4,
    'F': 2,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 0  # El objetivo tiene heurística 0
}

def a_star_tree_search(graph, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]  # (f(n), g(n), nodo, camino)
    while priority_queue:
        _, g, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path
        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            f = new_g + heuristic[neighbor]
            heapq.heappush(priority_queue, (f, new_g, neighbor, path + [neighbor]))
    return None

def a_star_graph_search(graph, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]  # (f(n), g(n), nodo, camino)
    visited = {}
    while priority_queue:
        _, g, node, path = heapq.heappop(priority_queue)
        if node == goal:
            return path
        if node not in visited or g < visited[node]:
            visited[node] = g
            for neighbor, cost in graph.get(node, []):
                new_g = g + cost
                f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue, (f, new_g, neighbor, path + [neighbor]))
    return None

# Ejecutar las búsquedas
start, goal = 'A', 'J'
path_tree = a_star_tree_search(graph, start, goal)
path_graph = a_star_graph_search(graph, start, goal)
print("Camino encontrado por A* Tree Search:", path_tree)
print("Camino encontrado por A* Graph Search:", path_graph)

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

# Mostrar el grafo con los caminos encontrados
draw_graph(graph, path_tree, "A* Tree Search - Camino encontrado")
draw_graph(graph, path_graph, "A* Graph Search - Camino encontrado")
