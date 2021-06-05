#EXERCÍCIO 1018
#Calcule o menor número possível de notas no qual o valor n1 pode ser decomposto
#notas: 100, 50, 20, 10, 5, 2 e 1
n1 = int(input())

n100 = n1 // 100
r = n1 % 100

n50 = r // 50
r = r%50

n20 = r // 20
r = r%20

n10 = r // 10
r = r%10

n5 = r // 5
r = r%5

n2 = r// 2
r = r % 2

n1 = r % 2

print(n1)
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
