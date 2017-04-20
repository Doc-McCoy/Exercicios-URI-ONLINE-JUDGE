# Exercicio referente ao problema numero 1040 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1040
# Por: Renan Santana Desiderio

n = raw_input().split(" ")
n1, n2, n3, n4 = n
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2 + n2*3 + n3*4 + n4* 1) / 10
print 'Media: %.1f' % media

if media >= 7.0:
	print 'Aluno aprovado.'
elif media < 5.0:
	print 'Aluno reprovado.'
else:
	print 'Aluno em exame.'
	exame = input()
	print 'Nota do exame: %.1f' % exame
	nova_media = (media + exame) /2

	if nova_media >= 5.0:
		print 'Aluno aprovado.'
	else:
		print 'Aluno reprovado.'
	print 'Media final: %.1f' % nova_media