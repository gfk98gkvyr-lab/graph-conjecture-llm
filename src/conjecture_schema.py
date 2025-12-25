from dataclasses import dataclass
from typing import Literal

Var = Literal["density", "avg_degree", "max_degree", "diameter"]
Op = Literal[">", ">=", "<", "<="]

@dataclass(frozen=True)
class Atom:
    var: Var
    op: Op
    value: float

@dataclass(frozen=True)
class Conjecture:
    premise: Atom   # IF
    conclusion: Atom  # THEN

def compare(x: float, op: Op, y: float) -> bool:
    if op == ">":  return x > y
    if op == ">=": return x >= y
    if op == "<":  return x < y
    if op == "<=": return x <= y
    raise ValueError("Unknown operator")

def atom_holds(atom: Atom, invariants: dict) -> bool:
    return compare(float(invariants[atom.var]), atom.op, float(atom.value))