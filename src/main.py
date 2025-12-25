from conjecture_generator import random_conjecture
from counterexample_search import find_counterexample

def main():
    n = 20
    conj = random_conjecture(n)
    print("Conjecture candidate:")
    print("IF", conj.premise, "THEN", conj.conclusion)

    ce = find_counterexample(conj, n=n, p=0.2, tries=8, steps=1200)

    if ce is None:
        print("Aucun contre-exemple trouvé (pour l'instant).")
    else:
        G, inv = ce
        print("✅ Contre-exemple trouvé ! Invariants:", inv)

if __name__ == "__main__":
    main()