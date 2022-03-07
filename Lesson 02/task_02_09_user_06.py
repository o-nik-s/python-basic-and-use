with open('input.txt') as f, open('output.txt', 'w') as w:
    for line in f.read().splitlines()[::-1]:
        w.write(line+'\n')