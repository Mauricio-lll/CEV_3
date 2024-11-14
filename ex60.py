# Faça um programa que leia um número qualquer e mostre o seu fatorial, usando estrutura while
def fatorial(numero):
  """Calcula o fatorial de um número.

  Args:
    numero: O número para o qual se deseja calcular o fatorial.

  Returns:
    O fatorial do número.
  """

  if numero == 0:
    return 1
  else:
    return numero * fatorial(numero - 1)

num = int(input("Digite um número para calcular o fatorial: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é {resultado}")

