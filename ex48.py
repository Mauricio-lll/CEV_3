# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontrar no intervalo de 1 até 500
soma = 0

# Iteramos de 1 até 500
for numero in range(1, 501):
    # Verificamos se o número é ímpar e múltiplo de 3
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print("A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {}".format(soma))


soma = 0
for numero in range(0,500):
    if numero%2!=0 and numero%3==0:
        soma += numero
print("A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {}".format(soma))
