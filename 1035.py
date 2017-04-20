# Exercicio referente ao problema numero 1035 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1035
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
a, b, c, d = n

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b>c and d>a and (c+d)>(a+b) and c>0 and d>0 and (a %2)==0:
	print "Valores aceitos"
else:
	print "Valores nao aceitos"