import random

def generate_random_graph(n, p):
    """
    Génère un graphe non orienté aléatoire (Erdős–Rényi).
    Représentation : dictionnaire {sommet: set(voisins)}
    """
    G = {i: set() for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                G[i].add(j)
                G[j].add(i)
    return G


def compute_density(G):
    n = len(G)
    m = sum(len(G[v]) for v in G) // 2
    if n <= 1:
        return 0.0
    return (2 * m) / (n * (n - 1))

from collections import deque

def average_degree(G):
    n = len(G)
    if n == 0:
        return 0
    return sum(len(G[v]) for v in G) / n


def max_degree(G):
    if not G:
        return 0
    return max(len(G[v]) for v in G)


def bfs_distances(G, start):
    distances = {start: 0}
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in G[u]:
            if v not in distances:
                distances[v] = distances[u] + 1
                queue.append(v)

    return distances


def diameter(G):
    if not G:
        return 0

    diam = 0
    for v in G:
        distances = bfs_distances(G, v)
        if len(distances) != len(G):
            return float("inf")  # graphe non connexe
        diam = max(diam, max(distances.values()))

    return diam