# Exercicio referente ao problema numero 1050 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1050
# Por: Renan Santana Desiderio

lista = {
	61:'Brasilia',
	71:'Salvador',
	11:'Sao Paulo',
	21:'Rio de Janeiro',
	32:'Juiz de Fora',
	19:'Campinas',
	27:'Vitoria',
	31:'Belo Horizonte'}

n = input()
while True: # esse laco eh necessario para usar try e except
	try:  # esse comando testara o que esta abaixo
		print lista[n] # caso nao de erro, ele executa ate o break
		break
	except: # caso de algum erro na linha acima, ele executa essa
		print 'DDD nao cadastrado' # excecao ate o break
		break