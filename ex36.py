#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o "valor da casa" o "Salário" do comprador e em "quantos anos" ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado
import math
from time import sleep

print('-'*15)
print('Seja muito bem vindo ao simulador de empréstimo para moradia')
print('-'*15)
print()
c = int(input('Qual o valor que você pretendo pagar na casa? R$ '))
s = int(input('Qual a sua renda mensal? R$ '))
t = int(input('Em quantos meses você deseja parcelar o empréstimo? '))
print('Deixa eu calcular aqui...')
sleep(2)
m = (s*0.3)
tt = (c/t)
if tt >= m:
    print('Com a sua renda, o empréstimo foi negado. Preferimos não comprometer seu renda.')
else:
    print("Muito bem, seu empréstimo foi aprovado. Suas parcelas serão de R${:.2f}.".format(c/t))