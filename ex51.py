#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. (Progressão Aritimética)
# No final, mostre os 10 primeiros termos dessa progressão
# Lendo o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Calculando e imprimindo os 10 primeiros termos
print("Os 10 primeiros termos da PA são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")