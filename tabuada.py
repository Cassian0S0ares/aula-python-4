valor = int(input("Valor da tabuada: "))
tabuada = 0
if valor >= 0:
    while tabuada <= 10:
        resultado = valor * tabuada
        print(f"o resultado é {resultado}")
        tabuada += 1
    print("W tabuada")
else:
    print("Valor positivo")