# Escreva um programa que leia dois números inteiros e compare-os, mostrando uma mensagem na tela
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior pois os dois são iguais
from time import sleep

n = int(input('Digite seu primeiro número: '))
m = int(input('E qual será seu segundo número? '))
print('Deixe-me comparar, 1 segundo...')
sleep(1)
if n>m:
    print('Parece que o número {} é maior que o número {}'.format(n,m))
elif n<m:
    print('Parece que o número {} é menor que {}'.format(n,m))
elif n==m:
    print('Parece que você escolheu o mesmo número duas vezes.')
print('Esses foram seus números!')