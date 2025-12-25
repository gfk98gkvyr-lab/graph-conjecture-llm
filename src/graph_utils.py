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