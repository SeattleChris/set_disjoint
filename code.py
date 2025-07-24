import os
from collections import defaultdict

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb: list[list[int]]):
    """Success except for 1 timeout limit (Test 17)."""
    lu_adj = defaultdict(list)
    for (a, b) in gb:
        lu_adj[a].append(b)
        lu_adj[b].append(a)
    lo, hi, used = float("inf"), 0, set()
    for key in lu_adj:
        if key in used:
            continue
        visited = {key}
        adj = [key]
        while adj:
            adj = [v for k in adj for v in lu_adj[k] if v not in visited]
            visited.update(adj)
        curr = len(visited)
        hi = curr if curr > hi else hi
        lo = curr if 1 < curr < lo else lo
        used |= visited
    return [lo, hi]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    gb = []
    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))
    result = componentsInGraph(gb)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
