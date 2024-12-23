connections: dict[str, set[str]] = {}

triple_sets = []

def BronKerbosch(R: set, P: set, X: set, potential_max = list()):
    if not P and not X:
        potential_max.append(R)
    
    while P:
        v = P.pop()
        P.add(v)
        n_v = connections[v]
        BronKerbosch(R.union({v}), P.intersection(n_v), X.intersection(n_v))
        P.remove(v)
        X.update({v})
    
    return potential_max
        

with open("test.txt") as f:
    for line in f:
        p1, p2 = line.strip().split("-")
        connections.setdefault(p1,set()).add(p2)
        connections.setdefault(p2,set()).add(p1)
    
    maxs = BronKerbosch(set(), set(connections.keys()),set())
    
    print(",".join(sorted(list(max(maxs, key=len))))) 