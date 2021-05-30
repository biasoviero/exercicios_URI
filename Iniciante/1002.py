#EXERCÍCIO 1002
#Escreva um programa que leia um valor correspondente ao raio de um círculo e calcule a sua área

raio = float(input())
pi = 3.14159
area = pi * raio **2

#:.xf indica quantas casas decimais a área tem
print('A={:.4f}'.format(area))
