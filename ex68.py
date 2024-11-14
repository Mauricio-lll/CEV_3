#Faça um programa que jogue 'par ou impar' com o computador. O jogo só será interrompido quando o jogador PERDER. mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
import random

def par_ou_impar():
    vitorias = 0

    while True:
        escolha_jogador = input("Escolha par ou ímpar (P/I): ").upper()
        numero_jogador = int(input("Digite um número: "))

        numero_computador = random.randint(1, 10)
        soma = numero_jogador + numero_computador
        resultado = "par" if soma % 2 == 0 else "impar"

        print(f"O computador jogou {numero_computador}.")
        print(f"A soma é {soma}, que é {resultado}.")

        if (escolha_jogador == "P" and resultado == "par") or (escolha_jogador == "I" and resultado == "impar"):
            print("Você ganhou!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break

    print(f"Você teve {vitorias} vitórias consecutivas.")

par_ou_impar()