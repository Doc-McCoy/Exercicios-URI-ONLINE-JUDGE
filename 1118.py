# Exercicio referente ao problema numero 1118 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1118
# Por: Renan Santana Desiderio

def media():
	while True:
		while True:
			nota1=input()
			if nota1>=0 and nota1<=10:
				break
			else:
				print "nota invalida"

		while True:
			nota2=input()
			if nota2>=0 and nota2<=10:
				break
			else:
				print "nota invalida"

		print "media = %.2f" %((float(nota1)+float(nota2))/2)
		while True:
			print "novo calculo (1-sim 2-nao)"
			x=input()

			if x==2:
				exit()
			elif x==1:
				media()
			else:
				continue
		break
media()