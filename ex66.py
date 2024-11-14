# Crie um programa que leia varios números interiros. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# no final mostre quantos numeros foram digitados e a soma entre eles
# Desconsiderando a flag
soma = cont = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} vezes e totalizou {soma}. ')