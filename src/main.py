from graph_utils import generate_random_graph, max_degree, compute_density, diameter
from graphity import generate_extreme_graphs

def main():
    n = 20
    p = 0.2

    def base_gen():
        return generate_random_graph(n, p)

    # objectif : maximiser le degré max
    objective = lambda G: float(max_degree(G))

    extreme = generate_extreme_graphs(base_gen, objective, k=5, steps=400)

    for i, G in enumerate(extreme, 1):
        print(f"--- Graphe extrême {i} ---")
        print("density =", compute_density(G))
        print("max_degree =", max_degree(G))
        print("diameter =", diameter(G))

if __name__ == "__main__":
    main()