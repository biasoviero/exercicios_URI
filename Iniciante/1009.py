#EXERCÍCIO 1009
#Leia o nome de um vendedor, seu salário e o total, em dinheiro, de suas vendas. Informe o total a receber
#O vendedor ganha 15% de comissão sobre as vendas feitas
nome = str(input())
salario = float(input())
vendas = float(input())
total = salario + (15/100 * vendas)
print('TOTAL = R$ {:.2f}'.format(total))
