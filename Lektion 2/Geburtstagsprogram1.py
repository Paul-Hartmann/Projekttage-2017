while True:

   Name = str(input("Wie heißt du (Mit Großschreibung bitte)?"))
   Jahr = int(input("In welchem Jahr bist du geboren?"))
   monat = int(input("In welchem Monat (als Zahl) hast du Geburtstag?"))
   tag = int(input("An welchem Tag (als Zahl) hast du Geburtstag?"))
   if tag == 28 and monat == 7:
       print("Herzlichen Glückwunsch zu deinem Geburtstag, Du wirst Heute", 2017-Jahr, "Jahre alt")

   elif (tag >=29 and monat == 7) or monat > 7:
       print("du bist", 2016-Jahr, "Jahre alt")

   elif tag < 28 and monat <= 7:
       print("du bist ", 2017-Jahr, "Jahre alt.")
      

   else:
       print("")
                   
    
   if Jahr > 2017:
      print("Du schumler")
      
   if monat==0 and tag == 0:
      print("Du schumelst")

   if monat == 0 or tag == 0:
      print("Du schumelst")

   elif Name == "Noelia":
         print("Du bist ein Arschgesicht")

   elif Name == "Frida":
      print("Du bist ein Argesicht")

   elif Name == "Jülide":
      print("Du bist ein Argesicht")

   elif Name == "Paul":
      print("Willkommen mein Gebieter")

   else:
      print("Good")
              

   antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

   if antwort != "yes":
      break
   else:
      print("\n\n")

   

