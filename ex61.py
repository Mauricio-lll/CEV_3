# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos de uma progressão usando a estrutura while
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f"O {contador}º termo é {termo}")
    termo += razao
    contador += 1