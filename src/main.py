from graph_utils import (
    generate_random_graph,
    compute_density,
    average_degree,
    max_degree,
    diameter
)

def main():
    G = generate_random_graph(10, 0.3)

    print("Densité :", compute_density(G))
    print("Degré moyen :", average_degree(G))
    print("Degré max :", max_degree(G))
    print("Diamètre :", diameter(G))

if __name__ == "__main__":
    main()