while True:

    print("Willkommen zur Quizshow ...\n !go or stand!")
    print("Nun auch gleich zu meiner ersten Frage")
    print("Wer schläft länger? \na) der Elefant b) die Giraffe\n c)das Faultier oder d) die Fledermaus")
    antwort = input("a), b), c), d)(schreiben sie es ohne Klammer)")
    if antwort == "d" or antwort == "d)":
        print("Glückwunsch das war richtig")
        print("Nun zur nächsten frage")
        print("Welchem afrikanischen Raubtier\n fallen am meisten Menschen zum Opfer?")
        antwort2 = input("a)Löwe, b)Jaguar,\n c)Krokodil d)Gepard")
    if antwort2 == "c" or antwort2 == "c)":
        print("Herzlichen Glückwunsch auch dass war richtig")
        print("weiter")
        print("Wie lang ist ein Tag auf dem Jupiter?")
        antwort3 = input("a) 9.50h b)24.00h c)12.20 d)22.40")
    if antwort3 == "a" or antwort3 == "a)":
        print("Sie haben es GESCHAFT ,fertig")

    else:
        print("Haha du Opfer")

        
    else:
        print("Haha du Opfer")


    else:
        print("HAHA du Opfer")
                
    antwort = input("\nWollen sie es noch einmal versuchen? (yes/no) ")

    if antwort != "yes":
       break
    else:
       print("\n\n")
