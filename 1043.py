# Exercicio referente ao problema numero 1043 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1043
# Por: Renan Santana Desiderio

n = raw_input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])

if ((b-c)<a<(b+c)) and ((a-c)<b<(a+c)) and ((a-b)<c<(a+b)):
	print "Perimetro = %.1f" % (a+b+c)

else:
	print "Area = %.1f" % (((a+b)*c)/2)