fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:   
    words = line.rstrip().split()
    for i in words:
        if len(lst) == 0:
            lst.append(i)
        elif i not in lst:
            lst.append(i)
        else:
            continue
lst.sort()
print(lst)
