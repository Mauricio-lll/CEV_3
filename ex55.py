# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e qual o menor peso.
pesos=[] #Cria uma lista para gravar os pesos

for c in range(5):
    peso = float(input("Qual o seu peso? "))
    pesos.append(peso) #Aqui ele arruma os pesos para float

maior_peso = max(pesos)
menor_peso = min(pesos)
print('O Maior peso é {:.2f} e o menor peso é {:.2f}'.format(maior_peso,menor_peso))