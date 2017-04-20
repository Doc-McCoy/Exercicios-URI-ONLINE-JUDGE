# Exercicio referente ao problema numero 1036 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1036
# Por: Renan Santana Desiderio

import math

n = raw_input().split(" ")
a, b, c = n

a = float(a)
b = float(b)
c = float(c)

delta = (b*b) - 4*a*c
if delta >0 and a!=0:
	x1 = (-b + math.sqrt(delta)) / (2*a)
	x2 = (-b - math.sqrt(delta)) / (2*a)
	print "R1 = %.5f" % x1
	print "R2 = %.5f" % x2
elif delta == 0 and a!=0:
	x1 = (-b + math.sqrt(delta)) / (2*a)
	print "R1 = %.5f" % x1

else:
	print "Impossivel calcular"