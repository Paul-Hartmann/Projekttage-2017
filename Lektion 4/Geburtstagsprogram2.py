while True:

   Jahr = int(input("In welchem Jahr bist du geboren?"))
   monat = str(input("In welchem Monat (mit Großschreibung) hast du Geburtstag?"))
   tag = int(input("An welchem Tag (als Zahl) hast du Geburtstag?"))

   a = ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"]

   monat = a.index(monat) +1
   if tag == 28 and monat == 7:
       print("Herzlichen Glückwunsch zu deinem Geburtstag, Du wirst Heute", 2017-Jahr, "Jahre alt")

   elif (tag >=29 and monat == 7) or monat > 7:
       print("du bist", 2016-Jahr, "Jahre alt")

   elif monat <7 or (monat == 7 and tag < 28):
       print("du bist ", 2017-Jahr, "Jahre alt.")
      

   else:
       print("")
                   
    
   if Jahr > 2017:
      print("Du schumler")
      
   if tag == 0:
      print("Du schumelst")
              

   antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

   if antwort != "yes":
      break
    
   else:
      print("\n\n")

   

