#EXERCÍCIO 1020
#Leia a idade de uma pessoa e expresse em anos, meses e dias
idade = int(input())
anos = idade // 365
r = idade % 365
meses = r // 30
r = r % 30
print(anos, 'ano (s)')
print(meses, 'mes (es)')
print(r, 'dia (s)')
