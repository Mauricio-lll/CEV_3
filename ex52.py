#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
import math
'''numero = int(input('Digite um número inteiro: '))
if numero <= 1:
    print('O número escolhido {}, NÃO é um número primo!'.format(numero))
for i in range(2, int(numero**0.5)+1):
    if numero % i == 0:
        print('O número escolhido {}, NÃO é um número primo!'.format(numero))
    elif numero <=1:
        print('O número escolhido {}, NÃO é um número primo!'.format(numero))
else:
    print('O número escolhido {}, é um número primo!'.format(numero))'''

def eh_primo(numero):
    """Verifica se um número é primo.

    Args:
        numero: O número a ser verificado.

    Returns:
        True se o número for primo, False caso contrário.
    """

    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Exemplo de uso:
numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")