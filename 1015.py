# Exercicio referente ao problema numero 1015 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015
# Por: Renan Santana Desiderio

linha1 = raw_input().split(" ")
linha2 = raw_input().split(" ")
x1, y1 = linha1
x2, y2 = linha2
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

import math

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print "%.4f" %distancia