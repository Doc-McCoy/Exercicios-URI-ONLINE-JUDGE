# Exercicio referente ao problema numero 1099 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1099
# Por: Renan Santana Desiderio

c = input()
soma = 0
for i in range(c):
	n = raw_input().split()
	x = int(n[0])
	y = int(n[1])
	l = [x,y]
	l.sort()
	x = l[0]
	y = l[1]
	for s in range(x+1,y):
		if s%2==1:
			soma+=s
	print "%i" %soma
	soma = 0