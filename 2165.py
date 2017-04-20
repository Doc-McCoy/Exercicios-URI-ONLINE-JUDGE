# Exercicio referente ao problema numero 2165 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2165
# Por: Renan Santana Desiderio

n = raw_input()
tam = len(n)
if tam < 141:
	print 'TWEET'
else:
	print 'MUTE'