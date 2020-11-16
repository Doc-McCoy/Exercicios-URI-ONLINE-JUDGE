# Exercicio referente ao problema numero 1069 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1069
# Por: Renan Santana Desiderio

test_cases = int(input())

for i in range(test_cases):
	content = input()
	left_side = 0
	# right_side = 0
	diamonds = 0
	for charactere in content:
		if charactere == '<':
			left_side += 1
		elif charactere == '>' and left_side > 0:
			diamonds += 1
			left_side -= 1
	print(diamonds)
