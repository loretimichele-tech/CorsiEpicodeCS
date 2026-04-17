#Datetime

import datetime


def assistente_virtuale(domanda):
    domanda = domanda.lower()

    if domanda == "data":
        oggi = datetime.datetime.now()
        risposta = "Oggi è il " + oggi.strftime("%d/%m/%Y") + " e comprate un calendario"
               
    elif domanda == "ora":
        ora_attuale = datetime.datetime.now().time()
        risposta = "Sono le " + ora_attuale.strftime("%H:%M") + "e comprate un orologio"

    elif domanda == "nome":
        risposta = "Fate i fatti toi"

    else: 
        risposta = "Va in Mona! Scrivi data, ora o nome."
    return(risposta)

while True:
    comando_utente = input("Cosa vuoi? ")
    if comando_utente.lower() == "esci":
        print("Ta do uno sciafon")
        break
    else: 
        print(assistente_virtuale(comando_utente))
