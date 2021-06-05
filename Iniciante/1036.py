#EXERCÍCIO 1036
#Leia os coeficientes a,b e c de uma equação de segundo grau. Em seguida, calcule as suas raízes
a, b, c = input().split()
a, b, c = [float(coeficiente) for coeficiente in [a, b, c]]

delta = b ** 2 - (4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular')

else:
    r1 = (-b + delta ** (1 / 2)) / (2 * a)
    r2 = (-b - delta ** (1 / 2)) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5F}'.format(r2))
    