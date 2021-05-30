#EXERCÍCIO 1008
#Leia um número correspondente a um funcionário, sua quantidade de horas trabalhadas, o valor que recebe por hora e calcule o seu salário

funcionario = int(input())
horas = int(input())
valor_por_hora = float(input())
salario = horas * valor_por_hora

print('NUMBER = {}'.format(funcionario))
print('SALARY = U$ {:.2f}'.format(salario))
