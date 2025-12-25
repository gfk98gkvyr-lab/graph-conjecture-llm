import random
from conjecture_schema import Atom, Conjecture

VARS = ["density", "avg_degree", "max_degree", "diameter"]
OPS = [">", ">=", "<", "<="]

def sample_threshold(var: str, n: int) -> float:
    if var == "density":
        return round(random.uniform(0.05, 0.95), 2)
    if var in ("avg_degree", "max_degree"):
        return float(random.randint(1, max(2, n-1)))
    if var == "diameter":
        return float(random.randint(1, max(2, n-1)))
    raise ValueError

def random_conjecture(n: int) -> Conjecture:
    a = random.choice(VARS)
    b = random.choice([v for v in VARS if v != a])

    premise = Atom(var=a, op=random.choice(OPS), value=sample_threshold(a, n))
    conclusion = Atom(var=b, op=random.choice(OPS), value=sample_threshold(b, n))

    return Conjecture(premise=premise, conclusion=conclusion)