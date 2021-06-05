#EXERCÍCIO 1017
#Leia o tempo gasto em uma viagem e a velocidade média. Calcule a distância percorrida e quantos litros são necessários.
tempo = int(input())
velocidade = int(input())
distancia = velocidade * tempo
litros = distancia / 12
print('{:.3f}'.format(litros))
