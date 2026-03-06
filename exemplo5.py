semvogal = ""
usuario_palavra = input("Entre com uma palavra: ")
usuario_palavra = usuario_palavra.upper()
for letra in usuario_palavra:
    if usuario_palavra == "SALSICHA":
        print("se vc sabe que a metade da salsicha é sal?")
        break
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra, end="")
