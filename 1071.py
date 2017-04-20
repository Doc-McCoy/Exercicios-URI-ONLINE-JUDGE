# Exercicio referente ao problema numero 1071 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1071
# Por: Renan Santana Desiderio

a = input() 	# recebe o valor de a
b = input() 	# recebe o valor de b
lista = [a,b] 	# transformei as duas variaveis em uma lista
lista.sort() 	# mandei ordenar a lista do menor pro maior
a = lista[0] 	# agora a = o primeiro numero da lista
b = lista[1] 	# e b = o segundo numero da lista
soma = 0 		# essa variavel vai ser a soma
#-------------------------------------------------------------------
for i in range(a+1,b):	# para cada numero de a ate b:
	if i%2!=0:			# caso o numero seja impar:
		soma+=abs(i)	# adicione ele mesmo a variavel 'soma'
print soma				# imprima a merda da soma