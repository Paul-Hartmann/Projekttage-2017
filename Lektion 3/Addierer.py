print("Ich bin ein Addierer!\n")

while True:

    zahl1 = int(input("Füge deine erste Zahl ein: "))
    zahl2 = int(input("Füge deine zweite Zahl ein: "))


    ergebnis = 0

    if zahl1 > 0:
        i = 0
        while i < zahl1:
            ergebnis +=1
            i+=1

    else:
        i=0
        while i>zahl1:
            ergebnis-=1
            i-=1


    if zahl2 > 0:  
        i = 0
        while i < zahl2:
            ergebnis +=1
            i+=1

    else:
        i=0
        while i>zahl2:
            ergebnis-=1
            i-=1
        
         
    print("Dein Ergebnis ist:", ergebnis)

    antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

    if antwort != "yes":
       break
    else:
       print("\n\n")
