def rec(a, b):
    an = 'No'
    if a in d[b]:
        return 'Yes'
    for i in d[b]:
        if i not in (':', b):
            an = rec (a, i)
            if an == 'Yes': return an
    return an

d = {}
for k in range(int(input())):
    line=input().split()
    d[line[0]]=line
for k in range(int(input())):
    line=input().split()
    print (rec(line[0],line[1]))