from typing import Dict, Set, Tuple
from graph_utils import compute_density, average_degree, max_degree, diameter
from conjecture_schema import Conjecture, atom_holds

Graph = Dict[int, Set[int]]

def compute_invariants(G: Graph) -> dict:
    d = diameter(G)
    return {
        "density": compute_density(G),
        "avg_degree": average_degree(G),
        "max_degree": float(max_degree(G)),
        "diameter": float(d) if d != float("inf") else float("inf"),
    }

def check_conjecture_on_graph(conj: Conjecture, G: Graph) -> Tuple[bool, bool, dict]:
    inv = compute_invariants(G)
    premise = atom_holds(conj.premise, inv)

    # Convention: si la prémisse est fausse, l'implication est vraie (logique)
    if not premise:
        return True, False, inv

    conclusion = atom_holds(conj.conclusion, inv)
    return conclusion, True, inv  # (holds?, premise_was_true?, invariants)