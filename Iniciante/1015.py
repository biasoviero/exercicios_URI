#EXERCÍCIO 1015
#Leia quatro valores que correspondem aos eixos x e y de dois pontos (x1, y1) e (x2, y2) e calcule a distância entre eles
import math
x1, y1 = [float(x) for x in input().split()]
x2, y2 =[float(x) for x in input().split()]
d = math.sqrt(((x2 - x1) ** 2 + (y2 - y1) ** 2)) 
print('{:.4f}'.format(d))
