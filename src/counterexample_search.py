from typing import Dict, Set, Optional, Tuple
from graphity import local_search
from graph_utils import generate_random_graph
from evaluator import check_conjecture_on_graph
from conjecture_schema import Conjecture

Graph = Dict[int, Set[int]]

def counterexample_objective(conj: Conjecture, G: Graph) -> float:
    holds, premise_true, inv = check_conjecture_on_graph(conj, G)

    # On veut: premise_true == True et holds == False
    if premise_true and (not holds):
        return 10.0  # jackpot: contre-exemple trouvé

    # Sinon on guide la recherche:
    # - on préfère les graphes où la prémisse est vraie (on s'en rapproche)
    # - on préfère ceux où la conclusion est fausse (on s'en rapproche)
    score = 0.0
    if premise_true:
        score += 2.0
    if not holds:
        score += 1.0
    return score

def find_counterexample(
    conj: Conjecture,
    n: int = 20,
    p: float = 0.2,
    tries: int = 10,
    steps: int = 1200,
) -> Optional[Tuple[Graph, dict]]:
    def base_gen():
        return generate_random_graph(n, p)

    for _ in range(tries):
        G0 = base_gen()
        Gbest = local_search(
            G0,
            objective=lambda G: counterexample_objective(conj, G),
            steps=steps,
            temperature=0.05,
            keep_edge_budget=True
        )
        holds, premise_true, inv = check_conjecture_on_graph(conj, Gbest)
        if premise_true and (not holds):
            return Gbest, inv

    return None