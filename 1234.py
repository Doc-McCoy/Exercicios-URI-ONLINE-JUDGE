# Exercicio referente ao problema numero 1234 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1234
# Por: Renan Santana Desiderio

n = list(raw_input())
out = list()
chave = True

for i in n:
	if i.isalpha():
		if chave:
			i=i.upper()
			chave=False
		else:
			i=i.lower()
			chave=True
	out.append(i)

out = ''.join(out)
print out