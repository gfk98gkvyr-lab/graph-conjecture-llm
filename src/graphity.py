import random
from typing import Callable, Dict, Set, Tuple, List

Graph = Dict[int, Set[int]]

def clone_graph(G: Graph) -> Graph:
    return {u: set(neigh) for u, neigh in G.items()}

def edge_count(G: Graph) -> int:
    return sum(len(G[u]) for u in G) // 2

def toggle_random_edge(G: Graph) -> Tuple[int, int, str]:
    """
    Ajoute ou supprime une arête aléatoire (u, v).
    Retourne (u, v, action) avec action in {"add", "remove"}.
    """
    n = len(G)
    u, v = random.sample(range(n), 2)
    if v in G[u]:
        G[u].remove(v)
        G[v].remove(u)
        return u, v, "remove"
    else:
        G[u].add(v)
        G[v].add(u)
        return u, v, "add"

def local_search_extreme(
    G0: Graph,
    objective: Callable[[Graph], float],
    steps: int = 300,
    temperature: float = 0.05,
) -> Graph:
    """
    Version simple type GraphiTy :
    - on part d'un graphe G0
    - on fait des mutations locales
    - on accepte les améliorations, et parfois des dégradations (pour éviter de bloquer)
    """
    G_best = clone_graph(G0)
    best_val = objective(G_best)

    G_cur = clone_graph(G0)
    cur_val = objective(G_cur)

    for _ in range(steps):
        G_new = clone_graph(G_cur)
        toggle_random_edge(G_new)
        new_val = objective(G_new)

        # acceptation : amélioration ou petit hasard (style recuit simulé simple)
        if new_val >= cur_val:
            G_cur, cur_val = G_new, new_val
        else:
            if random.random() < temperature:
                G_cur, cur_val = G_new, new_val

        # meilleur global
        if cur_val > best_val:
            G_best, best_val = clone_graph(G_cur), cur_val

    return G_best

def generate_extreme_graphs(
    base_generator: Callable[[], Graph],
    objective: Callable[[Graph], float],
    k: int = 20,
    steps: int = 300,
) -> List[Graph]:
    graphs = []
    for _ in range(k):
        G0 = base_generator()
        Gext = local_search_extreme(G0, objective, steps=steps)
        graphs.append(Gext)
    return graphs