import time
import webbrowser
valor = int(input("Valor da tabuada: "))
tabuada = 1
if valor > 0:
    print(f"Tabuada do {valor}")
    while tabuada <= 10:
        resultado = valor * tabuada
        print(f"o resultado é {resultado}")
        tabuada += 1
        time.sleep(1)
    print("W tabuada")
    time.sleep(1)
    webbrowser.open_new_tab("https://media.tenor.com/q4RChyNtpC8AAAAe/w-speed-ishowspeed.png")
else:
    print("Valor positivo porra")
    time.sleep(1)
    print("L total pra vc")
    time.sleep(1)
    webbrowser.open_new_tab("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0dehWfIbOwJGDavWz-cpPXRzx5kg8H9l_Sw&s")