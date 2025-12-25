import random
from typing import Callable, Dict, Set, Tuple, List, Optional

Graph = Dict[int, Set[int]]

def clone_graph(G: Graph) -> Graph:
    return {u: set(neigh) for u, neigh in G.items()}

def toggle_edge(G: Graph, u: int, v: int) -> str:
    """Ajoute ou supprime l'arête (u,v). Retourne 'add' ou 'remove'."""
    if v in G[u]:
        G[u].remove(v)
        G[v].remove(u)
        return "remove"
    else:
        G[u].add(v)
        G[v].add(u)
        return "add"

def random_edge_mutation(G: Graph) -> Tuple[int, int, str]:
    n = len(G)
    u, v = random.sample(range(n), 2)
    return u, v, toggle_edge(G, u, v)

def enforce_edge_budget(G: Graph, target_edges: int) -> None:
    """
    Optionnel: force le graphe à rester autour d'un nombre d'arêtes donné.
    Ça évite que 'max_degree' finisse toujours en graphe quasi-complet.
    """
    def edge_count(H: Graph) -> int:
        return sum(len(H[u]) for u in H) // 2

    n = len(G)
    # Ajustement grossier
    while edge_count(G) > target_edges:
        u, v = random.sample(range(n), 2)
        if v in G[u]:
            toggle_edge(G, u, v)
    while edge_count(G) < target_edges:
        u, v = random.sample(range(n), 2)
        if v not in G[u]:
            toggle_edge(G, u, v)

def local_search(
    G0: Graph,
    objective: Callable[[Graph], float],
    steps: int = 800,
    temperature: float = 0.03,
    keep_edge_budget: bool = False,
    target_edges: Optional[int] = None,
) -> Graph:
    """
    Recherche locale (style GraphiTy) :
    - on mutile une arête à la fois
    - on accepte toute amélioration
    - on accepte parfois une dégradation (température) pour ne pas bloquer
    - optionnel: on garde un budget d'arêtes pour éviter les solutions triviales
    """
    G_best = clone_graph(G0)
    best_val = objective(G_best)

    G_cur = clone_graph(G0)
    cur_val = objective(G_cur)

    n = len(G0)
    if keep_edge_budget and target_edges is None:
        # budget par défaut ~ densité 0.25
        target_edges = int(0.25 * (n * (n - 1) // 2))

    for _ in range(steps):
        G_new = clone_graph(G_cur)

        # Mutation locale
        random_edge_mutation(G_new)

        # Option: garder le même "ordre de grandeur" d'arêtes
        if keep_edge_budget and target_edges is not None:
            enforce_edge_budget(G_new, target_edges)

        new_val = objective(G_new)

        # acceptation
        if new_val >= cur_val:
            G_cur, cur_val = G_new, new_val
        else:
            if random.random() < temperature:
                G_cur, cur_val = G_new, new_val

        if cur_val > best_val:
            G_best, best_val = clone_graph(G_cur), cur_val

    return G_best

def generate_extreme_graphs(
    base_generator: Callable[[], Graph],
    objective: Callable[[Graph], float],
    k: int = 10,
    steps: int = 800,
    keep_edge_budget: bool = False,
    target_edges: Optional[int] = None,
) -> List[Graph]:
    out = []
    for _ in range(k):
        G0 = base_generator()
        Gext = local_search(
            G0,
            objective=objective,
            steps=steps,
            keep_edge_budget=keep_edge_budget,
            target_edges=target_edges,
        )
        out.append(Gext)
    return out