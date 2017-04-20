# Exercicio referente ao problema numero 1046 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1046
# Por: Renan Santana Desiderio

n = raw_input().split()
start = int(n[0])
end = int(n[1])
contador = 0
test = start

if (start==end):
	print "O JOGO DUROU 24 HORA(S)"
else:
	while (test!=end):
		test+=1
		contador+=1
		if (test==24):
			test=0
	print "O JOGO DUROU %i HORA(S)" % contador