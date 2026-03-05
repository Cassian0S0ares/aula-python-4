import time 
from datetime import datetime
while True:
    agora = datetime.now()
    horaatual = agora.strftime("%H:%M:%S")
    print(f"Hora atual: {horaatual}", end="\r")
    time.sleep(1)