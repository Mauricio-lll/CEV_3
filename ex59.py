# Crie um programa que leia dois valores e mostre um menu na tela.
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números
# [5] Sair do programa
# O programa deverá realizar a operação solciitada para cada caso
while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha uma opção:")
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")

    opcao = int(input("Digite sua opção (1-5): "))

    if opcao == 1:
        resultado = num1 + num2
        print(f"A soma é: {resultado}")
    elif opcao == 2:
        resultado = num1 * num2
        print(f"A multiplicação é: {resultado}")
    elif opcao == 3:
        maior = max(num1, num2)
        print(f"O maior número é: {maior}")
    elif opcao == 4:
        print("Digite os números novamente:")
        continue  # Volta para o início do loop
    elif opcao == 5:
        print("Saindo do programa...")
        break  # Sai do loop
    else:
        print("Opção inválida. Tente novamente.")