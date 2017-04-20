# Exercicio referente ao problema numero 1024 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1024
# Por: Renan Santana Desiderio

n = input()

for i in range(n):
	text = raw_input()
	text = list(text)
	# PRIMEIRA FASE ----------------------------
	for i in range(len(text)):
		if text[i].isalpha():
			text[i] = chr(ord(text[i])+3)
	# SEGUNDA FASE -----------------------------
	text.reverse()
	# TERCEIRA FASE ----------------------------
	for i in range((len(text)/2), (len(text))):
		text[i] = chr(ord(text[i])-1)
	text = "".join(text)
	print text