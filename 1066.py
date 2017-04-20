# Exercicio referente ao problema numero 1066 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1066
# Por: Renan Santana Desiderio

pos = 0
neg = 0
par = 0
imp = 0
for i in range(5):
	n = input()
	if n > 0:
		pos = pos+1
	elif n < 0:
		neg = neg+1
	if n%2==0:
		par=par+1
	elif n%2==1:
		imp=imp+1

print "%i valor(es) par(es)" % par
print "%i valor(es) impar(es)" % imp
print "%i valor(es) positivo(s)" % pos
print "%i valor(es) negativo(s)" % neg
