n=int(input())
nas={}
def poisk(A,B):
    global flag
    if A==B or A in nas[B]:
        flag=True
        return
    elif nas[B]==['None']:
        return
    else:
        for C in nas[B]:
            poisk(A,C)
for i in range(n):
    a=[i for i in input().split()]
    if len(a)==1:
        nas[a[0]]=['None']
    else:
        nas[a[0]]=a[2:]

p=int(input())
for i in range(p):
    a=[i for i in input().split()]
    flag=False
    poisk(a[0],a[1])
    if flag==True: print ('Yes')
    else: print('No')
