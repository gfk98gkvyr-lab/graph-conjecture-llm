from graph_utils import generate_random_graph, compute_density

def main():
    G = generate_random_graph(10, 0.3)
    density = compute_density(G)
    print("Densité du graphe :", density)

if __name__ == "__main__":
    main()
