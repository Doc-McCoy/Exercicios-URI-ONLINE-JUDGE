# Exercicio referente ao problema numero 2338 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/2338
# Por: Renan Santana Desiderio

morse = {
	'a':'=.===',
	'b':'===.=.=.=',
	'c':'===.=.===.=',
	'd':'===.=.=',
	'e':'=',
	'f':'=.=.===.=',
	'g':'===.===.=',
	'h':'=.=.=.=',
	'i':'=.=',
	'j':'=.===.===.===',
	'k':'===.=.===',
	'l':'=.===.=.=',
	'm':'===.===',
	'n':'===.=',
	'o':'===.===.===',
	'p':'=.===.===.=',
	'q':'===.===.=.===',
	'r':'=.===.=',
	's':'=.=.=',
	't':'===',
	'u':'=.=.===',
	'v':'=.=.=.===',
	'w':'=.===.===',
	'x':'===.=.=.===',
	'y':'===.=.===.===',
	'z':'===.===.=.=',
	' ':'.......'
}

t=input()
# O codigo abaixo inverte as chaves/valores do dicionario
# pra ficar mais facil de usar
morseInverse = dict((v,k) for (k,v) in morse.items())

for i in range(t):
	out = []
	n = raw_input()
	n = n.replace(".......", " ")
	n = n.split('...')
	for l in n:
		out.append(morseInverse[l])
	out = ''.join(out)
	print out