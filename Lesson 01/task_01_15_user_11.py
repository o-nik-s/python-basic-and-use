class_parents = dict()

def issubclass_(derived, parent):
    return parent == derived or any(issubclass_(class_parent, parent) for class_parent in class_parents[derived])

for class_input in [input() for _ in range(int(input()))]:
    words = class_input.replace(':', ' ').split()
    class_parents[words[0]] = words[1:]

queries = [input() for _ in range(int(input()))]
for parent, derived in (q.split() for q in queries):
    print('Yes' if issubclass_(derived, parent) else 'No')