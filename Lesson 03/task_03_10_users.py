# author
import re
import sys

for line in sys.stdin:
    line = line.strip()
    line = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
    print(line)




import re, sys

[print(re.sub(r'\b(\w)(\w)',r'\2\1', line.strip())) for line in sys.stdin]




import re, sys
exp = re.compile(r"\b(\w)(\w)(\w*)\b")
print(*map(lambda line: exp.sub(r'\2\1\3', line), sys.stdin), sep='')


