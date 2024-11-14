# Melhore o desafio 28 onde o computador pensa em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando quantos palpites foram necessários para vencer.
import random

# Computador pensa em um número entre 0 e 10
numero_secreto = random.randint(0, 10)
total_de_tentativas = 0

print("Tente adivinhar o número que estou pensando de 0 a 10.")

while True:
    chute = int(input("Qual é o seu palpite? "))
    total_de_tentativas += 1

    if chute < numero_secreto:
        print("Mais... Tente um número maior.")
    elif chute > numero_secreto:
        print("Menos... Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {total_de_tentativas} tentativas.")
        break
