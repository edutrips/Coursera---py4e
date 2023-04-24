# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
soma = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = float(line[line.find(' '):])
    count += 1
    soma += num
print(f'Average spam confidence: {soma/count}')

