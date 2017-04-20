# Exercicio referente ao problema numero 1073 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1073
# Por: Renan Santana Desiderio

n = input()

for i in range(n+1):
	if i%2==0 and i!=0:
		print "%i^2 = %i" % (i, i**2)