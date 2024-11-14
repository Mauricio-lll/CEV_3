primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
quantidade_termos = int(input("Digite quantos termos você quer mostrar (0 para sair): "))

termo = primeiro_termo
contador = 1

while quantidade_termos != 0:
    print(f"O {contador}º termo é {termo}")
    termo += razao
    contador += 1

    if contador > quantidade_termos:
        break  # Sai do loop se o contador ultrapassar a quantidade desejada

    quantidade_termos = int(input("Digite quantos termos você quer mostrar a mais (0 para sair): "))