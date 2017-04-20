# Exercicio referente ao problema numero 1037 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1037
# Por: Renan Santana Desiderio

n = input()

if n>=0 and n<=25:
	print "Intervalo [0,25]"
elif n>25 and n<=50:
	print "Intervalo (25,50]"
elif n>50 and n<=75:
	print "Intervalo (50,75]"
elif n>75 and n<=100:
	print "Intervalo (75,100]"
else:
	print "Fora de intervalo"