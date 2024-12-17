def somma():
    n1 = int(input("inserisci primo numero: "))
    n2 = int(input("inserisci secondo numero: "))
    print(f"{n1} + {n2} = {n1+n2}")

while True:
    print("Benvenuti nella nostra calcolatrice")
    print("Inserisci l'operazione che vuoi effettuare")
    scelta = int(input("1) sottrazione \n2) addizione \n 0) exit \n"))
    if scelta == 0:
        break
    elif scelta == 1:
        n1 = int(input("inserisci primo numero: "))
        n2 = int(input("inserisci secondo numero: "))
        print(f"{n1} - {n2} = {n1-n2}")

    elif scelta == 2:
        somma()

    else:
        print("valore non valido")
