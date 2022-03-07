from collections import defaultdict as dd
from itertools import product
dependencies, handled = dd(lambda: set()), set()
for _ in range(int(input())):
    inp = input().strip().split(":")
    if len(inp) > 1:
        for x, y in product(inp[1].strip().split(" "), [inp[0].strip()]):
            dependencies[x] |= {y}
for _ in range(int(input())):
    ex = input()
    if ex in handled:
        print(ex)
    stack = [ex]
    while stack:
        handled |= {stack[-1]}
        stack.extend(dependencies[stack.pop()])
