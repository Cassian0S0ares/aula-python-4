import time
numero = 0
while numero <= 10:
    if numero == 0:
        print(f"O numero: {numero} é zero")
        print(f"Meio redundante né?")
        numero += 1
        time.sleep(1)
    elif numero % 2 == 0:
        print(f"O numero: {numero} é par")
        numero += 1
        time.sleep(1)
    else:
        print(f"O numero: {numero} é impar")
        numero += 1
        time.sleep(1)
time.sleep(1)
print("W par ou impar")