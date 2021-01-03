# Exercicio referente ao problema numero 1087 do URI ONLINE JUDGE.
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1087
# Por: Renan Santana

while True:
    positions = input()
    x1, y1, x2, y2 = positions.split(" ")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 + y1 + x2 + y2 == 0:
        exit(0)

    plays = 0
    while x1 != x2 and y1 != y2:
        # Mover na diagonal
        if (x1 != x2 and y1 != y2) and (abs(x1 - x2) == abs(y1 - y2)):
            x1 = x2
            y1 = y2
            plays += 1
        # Mover na horizontal
        if x1 != x2:
            x1 = x2
            plays += 1
        # Mover na vertical
        if y1 != y2:
            y1 = y2
            plays += 1

    print(plays)
