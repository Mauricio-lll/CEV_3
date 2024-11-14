#Faça um programa que mostre na tela a 'contagem regressiva' para o estouro dos fogos, indo de 10 até 0 com uma pausa de 1 segunda entre eles
from time import sleep

for c in range(10,0, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')