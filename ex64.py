# Crie um programa que leia varios números inteiros pelo techado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (Desconsiderando o flag)
num = 0
soma = 0
contador = 0

while num != 999:
    num = int(input("Digite um número (999 para parar): "))
    if num != 999:
        soma += num
        contador += 1

print(f"Você digitou {contador} números.")
print(f"A soma dos números é {soma}.")