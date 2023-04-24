fname = input('enter the file name : ')
fopen = open(fname,'r')
dicionário = dict()
lst = list()
for line in fopen:
    sline = line.strip()
    if sline.startswith('From '):
        spline = sline.split()
        time = spline[5]
        tsplit = time.split(':')
        t1 = tsplit[0].split()
        for t in t1:
            dicionário[t] = dicionário.get(t, 0) + 1

for k,v in dicionário.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)