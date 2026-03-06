import random
import webbrowser
import time
tentativas = 3
numero = random.randint(1, 100)
while tentativas > 0:
    adivinha = int(input("Tente adivinhar o numero secreto: "))
    if adivinha > numero:
        print("O seu chute foi maior que o numero a ser adivinhado")
        tentativas -= 1
        print(f"Suas tentativas são {tentativas}")
    elif adivinha < numero:
        print("O seu chute foi menor que o numero a ser adivinhado")
        tentativas -= 1
        print(f"Suas tentativas são {tentativas}")
    else:
        print("Acertou :D")
        time.sleep(1)
        webbrowser.open_new_tab("https://media.tenor.com/q4RChyNtpC8AAAAe/w-speed-ishowspeed.png")
        break
if tentativas == 0:
    print("voce perdeu otario")
    print(f"O número era {numero}")
    time.sleep(1)
    webbrowser.open_new_tab("https://i.pinimg.com/originals/51/fd/1d/51fd1de984d5c3064afc29f7b6f0d21e.gif")
    