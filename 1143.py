# Exercicio referente ao problema numero 1143 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1143
# Por: Renan Santana Desiderio

n=input()

for i in range(n+1):
	if i!=0:
		print "%i %i %i" %(i, i**2, i**3)