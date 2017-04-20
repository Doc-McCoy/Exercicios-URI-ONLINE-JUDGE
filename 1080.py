# Exercicio referente ao problema numero 1080 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1080
# Por: Renan Santana Desiderio

cont=0
maior=0
for i in range(100):
	cont+=1
	n=input()
	if n>maior:
		posicao=cont
		maior=n
print "%i" % maior
print "%i" % posicao