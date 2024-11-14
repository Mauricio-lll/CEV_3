# Leia um número inteiro qualquer e peça para o usuário escolhar qual será a base de conversão
# 1 - Binário; 2 - Octal; 3 - Hexadecimal
def converter_base(numero, base):
  """
  Converte um número inteiro para a base especificada.

  Args:
    numero: O número inteiro a ser convertido.
    base: A base para a qual o número será convertido (1 para binário, 2 para octal, 3 para hexadecimal).

  Returns:
    Uma string representando o número na base especificada.
  """

  if base == 1:
    return bin(numero)[2:]
  elif base == 2:
    return oct(numero)[2:]
  elif base == 3:
    return hex(numero)[2:]
  else:
    return "Base inválida!"

if __name__ == "__main__":
  numero = int(input("Digite um número inteiro: "))

  print("Escolha a base de conversão:")
  print("1 - Binário")
  print("2 - Octal")
  print("3 - Hexadecimal")

  opcao = int(input("Digite a opção desejada: "))

  resultado = converter_base(numero, opcao)
  print("O número", numero, "convertido para a base", opcao, "é:", resultado)