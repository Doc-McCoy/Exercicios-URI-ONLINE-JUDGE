# Exercicio referente ao problema numero 1074 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1074
# Por: Renan Santana Desiderio

q = input()
for i in range(q):
	n = input()
	if n == 0:
		print "NULL"
	elif (n>0) and (n%2==0):
		print "EVEN POSITIVE"
	elif (n>0) and (n%2!=0):
		print "ODD POSITIVE"
	elif (n<0) and (n%2==0):
		print "EVEN NEGATIVE"
	elif (n<0) and (n%2!=0):
		print "ODD NEGATIVE"