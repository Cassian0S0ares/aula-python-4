numero = int(input("Coloque o seu numero: "))
array = [2, 3, 5, 7, 11]
for i in array:
    if numero % i == 0:
        print("Não é primo")
    else:
        print("É primo")