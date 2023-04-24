counts = {}
maior = 0 
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith('From '):
        line.rstrip()
        words = line.split()
        #print(words)
        for w in words:
            if '@' in w:
                if w in counts:
                    counts[w] = counts[w] + 1
                else:
                    counts[w] = 1
                if counts[w] > 0:
                    maior = counts[w]
                elif counts[w] > maior:
                    maior = counts[w]
            else:
                continue
for k, v in counts.items():
    if maior == v:
        print(k, v)
