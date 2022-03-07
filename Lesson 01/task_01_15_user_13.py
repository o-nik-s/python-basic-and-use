classes = {}
for i in range(int(input())):
    cl, *parents = input().split(' : ')
    classes.update({cl: parents[0].split() if len(parents) > 0 else []})


def find_parent(cls1, cls2):
    if cls1 == cls2:
        return True
    for cls in classes.get(cls2,[]):
        if cls == cls1 or find_parent(cls1, cls):
            return True


for i in range(int(input())):
    print('Yes' if find_parent(*input().split()) else 'No')
