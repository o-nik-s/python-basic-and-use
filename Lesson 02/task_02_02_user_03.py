my_cls = {}
mas2 = []
buf=[]
def is_parent(child, parent):
    return child == parent or any(map(lambda p: is_parent(p, parent), my_cls[child]))
for arg in [input().split() for x in range(int(input()))]:
    my_cls[arg[0]] = arg[2:len(arg)]
for arg in [input() for x in range(int(input()))]:
    mas2.append(arg)
mas2.reverse()
for arg in range(0, len(mas2)-1):
    buf.append(mas2[arg]) if any([is_parent(mas2[arg], mas2[x+1]) for x in range(arg, len(mas2)-1)]) else None
buf.reverse()
print("\n".join(buf))
