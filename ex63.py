# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci
def fibonacci(n):
    """Gera os n primeiros números da sequência de Fibonacci.

    Args:
        n: O número de termos da sequência.

    Returns:
        Uma lista com os n primeiros números da sequência de Fibonacci.
    """

    num1, num2 = 0, 1
    contador = 0
    sequencia = []

    while contador < n:
        sequencia.append(num1)
        prox = num1 + num2
        num1 = num2
        num2 = prox
        contador += 1

    return sequencia

while True:
    n = int(input("Digite quantos números da sequência de Fibonacci você deseja (0 para sair): "))
    if n == 0:
        break

    resultado = fibonacci(n)
    print(resultado)