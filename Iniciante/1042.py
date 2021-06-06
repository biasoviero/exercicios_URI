a, b, c = input().split()
a, b, c = [int(x) for x in [a, b, c]]
maior = max(a, b, c)
menor = min(a, b, c)
lista = [a, b, c]
lista.remove(maior)
lista.remove(menor)
print(menor, *lista, maior, sep = '\n')
print('')
print(*[a, b, c], sep = '\n')
