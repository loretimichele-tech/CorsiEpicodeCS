# Perimetro.py


forma = input("Inserisci Q per quadrato, C per cerchio o R per rettangolo per calcolare il perimetro / circonferenza: ")

forma = forma.upper().strip()
# dichiaro la variabile forma e abilito l'operatore a inserire l'input. 
# con upper prevengo errori di maiuscole / minuscole da parte dell'operatore

if forma == "Q":
    latoQ = float(input("Inserisci la lunghezza del lato: "))
    print(f"Perimetro quadrato: {latoQ * 4}")
elif forma == "C":
    latoC = float(input("Inserisci la lunghezza del raggio: "))
    print(f"Circonferenza cerchio: {latoC * 2 * 3.14}")
elif forma == "R":
    latoR = float(input("Inserisci la base del rettangolo: "))
    lato2 = float(input("Inserisci l'altezza del rettangolo: "))
    print(f"Perimetro rettangolo: {(latoR + lato2) * 2}")
else:
    print("Forma non riconosciuta. Usa Q, C o R.")

#dichiaro la condizione che viene abilitata dalla scelta dell'operatore e stampo il risultato

