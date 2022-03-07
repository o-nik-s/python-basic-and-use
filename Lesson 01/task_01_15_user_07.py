my_cls = {}
mas = set()
def find(a, b):
    global mas
    mas.update(my_cls[b])
    [find(a, i) for i in my_cls[b]]
    return mas
for arg in [input().split() for x in range(int(input()))]:
    my_cls[arg[0]] = arg[2:len(arg)]
for arg in [input().split() for x in range(int(input()))]:
    print('Yes') if arg[0] in find(arg[0], arg[1]) or arg[0] == arg[1] else print('No')
    mas.clear()