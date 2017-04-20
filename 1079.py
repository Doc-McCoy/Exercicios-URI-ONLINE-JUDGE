# Exercicio referente ao problema numero 1079 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1079
# Por: Renan Santana Desiderio

x=input()
for i in range(x):
	n=raw_input().split()
	a=float(n[0])
	b=float(n[1])
	c=float(n[2])
	print "%.1f" % (((a*2)+(b*3)+(c*5))/10)