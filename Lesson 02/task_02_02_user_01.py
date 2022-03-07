parents = {}

def check_parent(A, B):
    if (A == B):
        return True
    elif A in parents[B]:
        return True
    else:
        for i in parents[B]:
            if check_parent(A, i) == True:
                return True
    return False


for i in range(int(input())):
    line = input().split()
    parents [line[0]] = line[2:]

catch = []
for i in range(int(input())):
    catch.append(input())

for it in range(len(catch)):
    for parent in range(it):
        if check_parent(catch[parent], catch[it]):
            print(catch[it])
            break
