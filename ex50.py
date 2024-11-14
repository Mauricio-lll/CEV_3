#Desenvolva um programa que leia 'seis número inteiros' e mostre a soma daqueles que forem pares.
# Se for impar, desconsidere;
soma = 0
for c in range(6):
    escolha = int(input('Escolha um número: '))
    if escolha % 2 == 0:
        soma += escolha
print('A soma dos números pares é: {}'.format(soma))