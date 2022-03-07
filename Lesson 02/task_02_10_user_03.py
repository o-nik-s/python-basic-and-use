import os
print(*sorted(set(dir for dir, _, files in os.walk("main") for file in files if os.path.splitext(file)[1] == ".py")), sep="\n")