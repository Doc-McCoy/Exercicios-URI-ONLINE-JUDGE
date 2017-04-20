# Exercicio referente ao problema numero 1149 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1149
# Por: Renan Santana Desiderio

l = raw_input().split()
a = int(l[0])
n = int(l[1])
soma = 0
while True:
	if n>0:
		break
	else:
		n = input()

for i in range(a, a+n):
	soma+=i

print soma