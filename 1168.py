# Exercicio referente ao problema numero 1168 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1168
# Por: Renan Santana Desiderio

leds = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}
n = input()
soma = 0
for i in range(n):
	soma = 0
	valor = list(raw_input())
	for v in valor:
		for d in leds:
			if int(v)==d:
				soma = soma+leds[d]
	print "%i leds" % soma