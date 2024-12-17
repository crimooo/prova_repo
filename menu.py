import calcolatrice as clc

while True:
    print()
    print("Benvenuti nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1) sottrazione \n2) addizione \n 0) exit \n"))
    if scelta == 0:
        break
    elif scelta == 1:
        clc.sottrazione
        
    elif scelta == 2:
        clc.somma

    else:
        print("valore non valido")
