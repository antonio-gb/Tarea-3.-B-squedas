import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Grafo con heurística (valores arbitrarios)
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

def greedy_best_first_search(graph, start, goal):
    priority_queue = [(heuristic[start], start, [start])]  # (h(n), nodo, camino)
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)  # Extrae el nodo con menor heurística

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None  # No se encontró camino

# Ejecutar la búsqueda
start, goal = 'A', 'J'
path = greedy_best_first_search(graph, start, goal)
print("Camino encontrado por Greedy Best-First Search:", path)

# Visualizar el grafo
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
draw_graph(graph, path, "Greedy Best-First Search - Camino encontrado")
