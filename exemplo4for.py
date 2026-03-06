print("Comando Break")
for i in range(1, 6):
    if i == 3:
        break
    print("dentro do loop", i)
print("fora do loop")
print("\nComando continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("dentro do loop", i)
print("fora do loop")
