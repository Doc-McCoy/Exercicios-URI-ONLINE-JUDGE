# Exercicio referente ao problema numero 1253 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1253
# Por: Renan Santana Desiderio

def decode(word, offset):
    result = []
    for letter in word:
        letter_value = ord(letter)
        letter_value -= offset
        if letter_value < 65:
            letter_value += 26
        if letter_value > 90:
            letter_value -= 26
        resultant_letter = chr(letter_value)
        result.append(resultant_letter)
    return ''.join(result)

entradas = int(input())

for i in range(entradas):
    secret_word = input()
    offset = int(input())
    result = decode(secret_word, offset)
    print(result)
