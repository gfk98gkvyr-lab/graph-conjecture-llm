from graph_utils import generate_random_graph, compute_density, max_degree, diameter
from graphity import generate_extreme_graphs

def main():
    n = 20
    p = 0.2

    def base_gen():
        return generate_random_graph(n, p)

    # Objectif 1: maximiser max_degree (mais en gardant un budget d'arêtes)
    target_edges = int(0.25 * (n * (n - 1) // 2))  # ~densité 0.25
    graphs_hub = generate_extreme_graphs(
        base_gen,
        objective=lambda G: float(max_degree(G)),
        k=3,
        steps=900,
        keep_edge_budget=True,
        target_edges=target_edges
    )

    print("=== EXTREMES: MAX DEGREE ===")
    for i, G in enumerate(graphs_hub, 1):
        print(f"[hub {i}] density={compute_density(G):.3f} max_degree={max_degree(G)} diameter={diameter(G)}")

    # Objectif 2: maximiser diameter (aussi avec budget d'arêtes pour éviter graphe trop dense)
    graphs_long = generate_extreme_graphs(
        base_gen,
        objective=lambda G: float(diameter(G)) if diameter(G) != float("inf") else -1.0,
        k=3,
        steps=1200,
        keep_edge_budget=True,
        target_edges=target_edges
    )

    print("\n=== EXTREMES: DIAMETER ===")
    for i, G in enumerate(graphs_long, 1):
        print(f"[long {i}] density={compute_density(G):.3f} max_degree={max_degree(G)} diameter={diameter(G)}")

if __name__ == "__main__":
    main()