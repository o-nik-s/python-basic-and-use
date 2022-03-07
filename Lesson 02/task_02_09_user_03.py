with open("123.txt") as f, open("123_copy.txt", "w") as f2:
  for line in reversed(list(f)):
    f2.write(line)