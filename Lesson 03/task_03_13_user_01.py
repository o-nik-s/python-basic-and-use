import requests, re
A, B, T = input(), input(), re.compile(r'<a\s+href\s*=\s*"(.+)"')
print("Yes" if B in (D for C in T.findall(requests.get(A).text) for D in T.findall(requests.get(C).text)) else "No")