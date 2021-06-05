#EXERCÍCIO 1019
#Leia o tempo de duração em segundos e mostre o seu formato em horas:minutos:segundos
N = int(input())
horas = N // 3600
r = N%3600
minutos = r // 60
r = r%60
print('{}:{}:{}'.format(horas, minutos, r))
