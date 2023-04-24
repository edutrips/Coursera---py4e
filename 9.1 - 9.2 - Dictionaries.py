purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse ['candy'] + 2
print(purse)
#método get
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#if name in counts:
 #   x = counts[name]
#else:
 #   x = 0
#é igual a:
# x = counts.get(name, 0) # 0 é o valor que eu retorno
#se a chave não existir, se ela existir, ele me retorna o valor dela
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)