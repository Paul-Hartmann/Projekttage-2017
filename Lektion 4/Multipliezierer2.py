while True:

    Zahl = int(input("Bitte geben sie eine Zahl ein:"))

    for i in range(1,11,1):
        print(i,"*",Zahl,"=",i*Zahl)

    
    antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

    if antwort != "yes":
      break
    else:
       print("\n\n")

