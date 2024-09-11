print("Quer saber qual foi seu aumento de salario?")
salario = float(input ("quanto vc ganha atualmente?"))
porcentagemaumento = float(input("qual foi a porcentagem de aumento que vc recebeu"))



calculo = porcentagemaumento * salario / 100
novosalario = salario + calculo
print(f"o aumento do seu salario foi de {calculo}")
print(f" seu novo salario é de {novosalario}")

