#EXERCÍCIO 1038
codigo, quantidade = input().split()
codigo, quantidade = [float(x) for x in [codigo, quantidade]]
if codigo == 1:
    total = quantidade * 4
if codigo == 2:
    total = quantidade * 4.5
if codigo == 3:
    total = quantidade * 5
if codigo == 4:
    total = quantidade * 2
if codigo == 5:
    total = quantidade * 1.5
print('Total: R$ {:.2f}'.format(total))
