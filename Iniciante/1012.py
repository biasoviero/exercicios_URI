#EXERCÍCIO 1012
#leia três valores com ponto flutuante (A, B e C) mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B. 

a, b, c = [float(x) for x in input().split()]

triangulo = (a * c)/2.0
circulo = 3.14159 * c ** 2
trapezio = ((a + b) * c)/2.0
quadrado = b ** 2
retangulo = a * b

print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))