# Exercicio referente ao problema numero 1049 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049
# Por: Renan Santana Desiderio

n1 = raw_input()
n2 = raw_input()
n3 = raw_input()

if n1 == 'vertebrado':
	if n2 == 'ave':
		if n3 == 'carnivoro':
			print 'aguia'
		elif n3 == 'onivoro':
			print 'pomba'
	elif n2 == 'mamifero':
		if n3 == 'onivoro':
			print 'homem'
		elif n3 == 'herbivoro':
			print 'vaca'

elif n1 == 'invertebrado':
	if n2 == 'inseto':
		if n3 == 'hematofago':
			print 'pulga'
		elif n3 == 'herbivoro':
			print 'lagarta'
	elif n2 == 'anelideo':
		if n3 == 'hematofago':
			print 'sanguessuga'
		elif n3 == 'onivoro':
			print 'minhoca'