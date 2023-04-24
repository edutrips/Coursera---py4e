import re
y = 0
fname = input('File name: ')
if len(fname) <= 1:
    fh = open('actualdata.txt')
else:
    fh = open(fname)
for line in fh:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for i in x:
        y += int(i)

print(y)