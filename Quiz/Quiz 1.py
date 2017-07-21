while True:

    print("Willkommen zur Quizshow ...\n !go or stand!")
    print("Nun auch gleich zu meiner ersten Frage")
    print("Wer schläft länger? \na) die Fledermaus b) die Giraffe\n c)das Faultier oder d) Der Elefant")
    antwort = input("a), b), c), d)")
    if antwort == "a" or antwort == "a)":
        print("Glückwunsch das war richtig")
        print("Nun zur nächsten frage")
        print("Welchem afrikanischen Raubtier\n fallen am meisten Menschen zum Opfer?")
        antwort2 = input("a)Krokodil b)Jaguar,\n c)Löwe d)Gepard")
    if antwort2 == "a" or antwort2 == "a)":
        print("Herzlichen Glückwunsch auch dass war richtig")
        print("weiter")
        print("Wie lang ist ein Tag auf dem Jupiter?")
        antwort3 = input("a) 9.50h b)24.00h c)12.20 d)22.40")
    if antwort3 == "a" or antwort3 == "a)":
        print("Sie haben es GESCHAFT ,fertig")

    else:
        print("Haha du Opfer")

        
                 
    antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

    if antwort != "yes":
       break
    else:
       print("\n\n")
