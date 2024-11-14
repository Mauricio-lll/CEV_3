#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço; Se é hora de se alistar; - Se já passou do tempo do alistamento;
# Deverá mostrar quanto tempo falta ou quanto tempo passou do prazo;
import calendar
from datetime import date
print('='*20)
print('Bem vindo ao seu controle de alistamento militar')
print('='*20)
d = int(input('Em que ano você nasceu? '))
a = 18
b = (date.today().year-d)
if d>date.today().year:
    print('Ops, parece que você ainda nem nasceu!')
elif b<a:
    print('Parece que você ainda tem {} ano(s) para o seu alistamento'.format(a-b))
elif b>a:
    print('Seu alistamento já passou, foi à {} ano(s)'.format(b-a))
else:
    print('Não perca tempo, você deve cumprir o alistamento militar neste ano. ')