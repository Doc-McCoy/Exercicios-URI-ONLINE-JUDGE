# Exercicio referente ao problema numero 1120 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1120
# Por: Renan Santana Desiderio

while True:
	n = raw_input().split()
	ref = n[0]
	numero = list(n[1])
	result = ['0']
	if int(ref)==0 and int(''.join(numero))==0:
		break
	# ----------------------
	for i in numero:
		if i != ref:
			result.append(i)
	result = int(''.join(result))
	print result