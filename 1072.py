# Exercicio referente ao problema numero 1072 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1072
# Por: Renan Santana Desiderio

n = input()
inn = 0
out = 0
for i in range(n):
	m = input()
	if m>=10 and m<=20:
		inn+=1
	else: 
		out+=1
print "%i in" % inn
print "%i out" % out
