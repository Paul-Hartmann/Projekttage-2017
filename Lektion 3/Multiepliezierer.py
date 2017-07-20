print("Ich bin ein Multipliezierer!\n")


while True:

    zahl1 = int(input("Zahl1: "))
    zahl2 = int(input("Zahl2: "))

    ergebnis = 0

    if (zahl1 > 0 and zahl2 > 0) or (zahl1 < 0 and zahl2 < 0):
            
        if zahl1 < 0 and zahl2 < 0:
            zahl1 = zahl1 * (-1)
            zahl2 = zahl2 * (-1)
                
        i = 0
        while i < zahl1:
            j = 0
            while j < zahl2:
                ergebnis += 1
                j += 1
            i += 1

    else:

        if zahl1 < 0:
            zahl1 = zahl1 * (-1)
        else:
            zahl2 = zahl2 * (-1)

        i = 0
        while i < zahl1:
            j = 0
            while j < zahl2:
                ergebnis -= 1
                j += 1
            i += 1



                 
    print("Dein Ergebnis ist:", ergebnis)



    antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

    if antwort != "yes":
       break
    else:
       print("\n\n")


