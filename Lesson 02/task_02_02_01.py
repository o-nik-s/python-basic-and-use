n = int(input())
inheritanceList = {}
for _ in range(n):
    inheritanceDescr = input().strip()
    inheritanceList[inheritanceDescr.split(":")[0].strip()] = [] if ":" not in inheritanceDescr \
        else inheritanceDescr.split(":")[1].split()
# print(inheritanceList)

m = int(input())
exceptionList = set()
for _ in range(m):
    exceptionNow = input().strip()
    is_child = any(map(lambda p: p in exceptionList, inheritanceList[exceptionNow]))
    print(exceptionNow) if is_child else exceptionList.add(exceptionNow)
