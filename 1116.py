# Exercicio referente ao problema numero 1116 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1116
# Por: Renan Santana Desiderio

t = input()
for i in range(t):
	n = raw_input().split()
	x = float(n[0])
	y = float(n[1])
	if y==0:
		print "divisao impossivel"
	else:
		print "%.1f" % (x/y)