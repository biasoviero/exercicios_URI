#EXERCÍCIO 1021
#Leia um valor monetário e calcule o menor número de notas e moedas em que o valor pode ser decomposto
#Notas: 100, 50, 20, 10, 5, 2
#Moedas: 1, 0.50, 0.25, 0.10, 0.05 e 0.01
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    quantidade_n = int(valor / nota)
    
    print('{} nota(s) de R$ {:.2f}'.format(quantidade_n, nota))
    valor -= quantidade_n * nota

print('MOEDAS:')
for moeda in moedas:
    quantidade_m = int(round(valor, 2) / moeda)

    print('{} moeda(s) de R$ {:.2f}'.format(quantidade_m, moeda))
    valor -= quantidade_m * moeda
