#EXERCÍCIO 1013
# Leia três valores e apresente o maior entre eles.

a, b, s = [int(x) for x in input().split()]
maior = max(a, b, s)
print('{} eh o maior'.format(maior))
