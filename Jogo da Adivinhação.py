#Adivinhação

import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Digite um número de 1 a 100: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")