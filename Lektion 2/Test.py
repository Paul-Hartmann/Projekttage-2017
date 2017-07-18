Jahr = int(input("In welchem Jahr bist du geboren?"))
monat = int(input("In welchem Monat (als Zahl) hast du Geburtstag?"))
tag = int(input("An welchem Tag (als Zahl) hast du Geburtstag?"))
if tag == 18 and monat == 7:
   print("Herzlichen Glückwunsch zu deinem Geburtstag, Du wirst Heute", 2017-Jahr, "Jahre alt")

elif tag >=19 and monat >= 7:
    print("du bist", 2016-Jahr, "Jahre alt")

elif tag < 18 and monat <= 7:
    print("du bist ", 2017-Jahr, "Jahre alt.")
   

else:
    print("")
                
