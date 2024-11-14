# Crie um programa que leia varios números inteiros pelo techado. Mostre a média entre todos os valores e qual foi o maior e o menos valor lido.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
numeros = []
continuar = 'S'

while continuar == 'S':
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    continuar = input("Quer continuar? [S/N] ").upper()

if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    maior = max(numeros)
    menor = min(numeros)
    print(f"A média dos números é: {media:.2f}")
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
else:
    print("Nenhum número foi digitado.")