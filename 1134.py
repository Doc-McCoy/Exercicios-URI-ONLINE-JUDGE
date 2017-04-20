# Exercicio referente ao problema numero 1134 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1134
# Por: Renan Santana Desiderio

alc=0
gas=0
die=0
choose=0
while choose!=4:
	choose=input()
	if choose==1:
		alc+=1
	elif choose==2:
		gas+=1
	elif choose==3:
		die+=1
print 'MUITO OBRIGADO'
print 'Alcool: %i' %alc
print 'Gasolina: %i' %gas
print 'Diesel: %i' %die