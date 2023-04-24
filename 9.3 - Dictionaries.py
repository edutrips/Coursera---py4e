counts = {}
fh = open('words1.txt')
for line in fh:
    print(line)
    words = line.split()
    for i in words:
        if i not in counts:
            counts['Palavras'] = i
        elif i in counts:
            counts['Palavras'] = i
print(counts.values())
for i in counts:
    print(i)