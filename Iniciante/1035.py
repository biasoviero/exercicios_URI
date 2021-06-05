#EXERCÍCIO 1035
#Leia valores a, b, c e d. Se b > c, se d > a, c + d > a + b , se c e d forem positivos e se a for par escreva "Valores aceitos", senão escreva "Valores nao aceitos"
A, B, C, D = input().split()
valores = [int(valor) for valor in [A, B, C, D]]

if B > C and D > A and C + D > A + B: 
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
