print("bem vindo a calculadora de consumo medio")

distancia = float(input ("quantos km voce andou ?"))
combustivel = float(input("quantos litros foram gastos em sua viajem ?"))
valorcombustivel = float(input(" qual o valor do combustivel?"))

media = distancia / combustivel
mediapreço = valorcombustivel * combustivel
print(f"seu consumo médio é de {media}")
print(f"o valor gasto com combustivel é de: {mediapreço}")               
                
