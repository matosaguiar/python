print("Bem-vindo ao orçamento do carro que você alugou")

kmpercorrido = float(input("Escreva quantos km você percorreu: "))
diasdeuso = float(input("Escreva quantos dias você usou o carro: "))


calculo = diasdeuso * 60
calculo2 = kmpercorrido * 0.15
calculo3 = calculo + calculo2


print(f"O custo do aluguel foi de R$ {calculo}, já os km rodados foi de R$ {calculo2}")
print(f"O valor total foi de: R$ {calculo3}")
