#Refaça o desafio 09 mostrando a tabuada de um número que o usuário escolhar, só que agora faça usando "for"
print("\nPrograma para TABUADA.")
n = int ( input("\nDigite um número inteiro para ver sua tabuada"))
print("\nA tabuada de {} será apresentada abaixo:".format(n))
print(15*"-")
for i in range (11):
  print("{} x {} = {:2}".format(n,i,n*i))
print(15*"-")