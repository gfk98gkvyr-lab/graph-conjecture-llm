# src/main.py
"""
Point d'entrée du projet (démo).

But :
- générer une conjecture,
- chercher automatiquement un contre-exemple,
- sauvegarder un résumé des résultats dans /results (JSON),
- sauvegarder une visualisation (PNG) d'un graphe exemple,
  et du contre-exemple s'il est trouvé.

Lancer :
python src/main.py --n 20 --p 0.2 --tries 8 --steps 1200 --seed 42
"""

import argparse
import json
import os
import random
import time

import matplotlib.pyplot as plt
import networkx as nx

from conjecture_generator import random_conjecture
from counterexample_search import find_counterexample


def set_seed(seed: int) -> None:
    """Reproductibilité : même seed => mêmes tirages aléatoires (au maximum)."""
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except Exception:
        pass


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def project_root_dir() -> str:
    """Racine du projet = dossier parent de src/"""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def serialize_graph(G):
    """Sauvegarde simple : nb noeuds, nb arêtes, liste d'arêtes (limitée)."""
    data = {"repr": repr(G)}
    try:
        data["num_nodes"] = int(G.number_of_nodes())
        data["num_edges"] = int(G.number_of_edges())
        edges = list(G.edges())
        data["edges"] = [(int(u), int(v)) for u, v in edges[:2000]]
        data["edges_truncated"] = len(edges) > 2000
    except Exception:
        data["note"] = "Impossible de sérialiser finement ce graphe (type inconnu)."
    return data


def save_graph_png(G, path: str, seed: int = 42) -> None:
    """Sauvegarde une image propre d'un graphe NetworkX en PNG."""
    plt.figure(figsize=(7, 7))
    pos = nx.spring_layout(G, seed=seed)  # layout stable
    nx.draw_networkx_nodes(G, pos, node_size=220)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.85)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(path, dpi=220)
    plt.close()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20, help="Taille des graphes (paramètre n)")
    parser.add_argument("--p", type=float, default=0.2, help="Paramètre p")
    parser.add_argument("--tries", type=int, default=8, help="Nombre d'essais (tries)")
    parser.add_argument("--steps", type=int, default=1200, help="Nombre d'étapes (steps)")
    parser.add_argument("--seed", type=int, default=0, help="Seed pour reproductibilité")
    parser.add_argument("--out", type=str, default="results", help="Dossier de sortie")
    return parser.parse_args()


def main():
    args = parse_args()
    set_seed(args.seed)

    out_dir = os.path.join(project_root_dir(), args.out)
    ensure_dir(out_dir)

    start = time.time()

    print(f"[INFO] Params: n={args.n}, p={args.p}, tries={args.tries}, steps={args.steps}, seed={args.seed}")

    # 0) Graphe exemple (toujours) -> PNG pour le rapport
    G_example = nx.erdos_renyi_graph(args.n, args.p, seed=args.seed)
    example_png = os.path.join(out_dir, f"example_graph_n{args.n}_p{args.p}_seed{args.seed}.png")
    save_graph_png(G_example, example_png, seed=args.seed)
    print(f"[INFO] Example graph saved: {example_png}")

    # 1) Conjecture
    conj = random_conjecture(args.n)
    print("\n=== Conjecture candidate ===")
    print("IF   ", conj.premise)
    print("THEN ", conj.conclusion)

    # 2) Recherche de contre-exemple
    ce = find_counterexample(conj, n=args.n, p=args.p, tries=args.tries, steps=args.steps)

    found = ce is not None
    ce_payload = None

    if not found:
        print("\nAucun contre-exemple trouvé (dans les limites testées).")
    else:
        try:
            G, inv = ce  # attendu: (Graphe, invariants)
            ce_payload = {"graph": serialize_graph(G), "invariants": inv}

            # PNG du contre-exemple
            ce_png = os.path.join(out_dir, f"counterexample_seed{args.seed}.png")
            save_graph_png(G, ce_png, seed=args.seed)
            print(f"[INFO] Counterexample image saved: {ce_png}")

            print("\n✅ Contre-exemple trouvé !")
            ginfo = ce_payload["graph"]
            if "num_nodes" in ginfo:
                print(f"  - nodes={ginfo['num_nodes']} edges={ginfo.get('num_edges', '?')}")
            print(f"  - invariants: {inv}")
        except Exception:
            ce_payload = {"raw": repr(ce)}
            print("\n✅ Contre-exemple trouvé ! (format non standard)")

    elapsed = time.time() - start

    # 3) JSON résultat
    result = {
        "seed": args.seed,
        "n": args.n,
        "p": args.p,
        "tries": args.tries,
        "steps": args.steps,
        "conjecture": {"premise": str(conj.premise), "conclusion": str(conj.conclusion)},
        "found_counterexample": found,
        "counterexample": ce_payload,
        "elapsed_seconds": elapsed,
        "artifacts": {
            "example_png": os.path.basename(example_png),
        },
    }

    filename = f"run_n{args.n}_p{args.p}_tries{args.tries}_steps{args.steps}_seed{args.seed}.json"
    out_path = os.path.join(out_dir, filename)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print("\n=== Résumé ===")
    print(f"seed={args.seed} n={args.n} p={args.p} tries={args.tries} steps={args.steps}")
    print(f"found_counterexample={found}")
    print(f"elapsed_seconds={elapsed:.3f}")
    print(f"Saved: {out_path}\n")


if __name__ == "__main__":
    main()
