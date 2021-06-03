#EXERCÍCIO 1010
#Leia o código, o número de peças, o valor unitário de peças 1 e 2. Mostre o valor a ser pago

linha1 = input().split()
c1 = int(linha1[0])
n1 = int(linha1[1])
v1 = float(linha1[2])

#.split() permite inserir vários valores a uma só variável. 

linha2 = input().split()
c2 = int(linha2[0])
n2 = int(linha2[1])
v2 = float(linha2[2])
total = (n1 * v1) + (n2 * v2)
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
