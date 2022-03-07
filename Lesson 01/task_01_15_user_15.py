dependencies = {}
for _ in range(int(input())):
    inp = input().strip().split(":")
    dependencies.update([(inp[0], []) if len(inp) == 1 else (inp[0].strip(), inp[1].strip().split())])
classes = {c for c in dependencies} | {sc for c in dependencies for sc in c}
for _ in range(int(input())):
    e, s = input().strip().split()
    stk, route = [s], False
    while(stk and not route):
        stk.extend(dependencies[stk.pop()])
        route = (stk[-1] == e) if stk else False
    print("Yes" if route or e == s and s in classes else "No")