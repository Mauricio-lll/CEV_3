# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
print("\nPrograma para TABUADA.")
while True:
    n = int ( input("\nDigite um número inteiro para ver sua tabuada: "))

    if n < 0:
        break

    for i in range (11):
        print(f'{n} x {i} = {n*i:2}')
'''while True:
    numero = int(input("Digite um número para ver sua tabuada (negativo para sair): "))

    if numero < 0:
        break

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")'''