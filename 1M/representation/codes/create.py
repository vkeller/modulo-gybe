trad = int(input("ASCII -> decimal (1), Decimal/binaire/Hexa -> ASCII (2)"))

if trad == 1 :
    fin = False
    print("ASCII -> Decimal (é pour sortir")
    phrase = ""
    phrase_d = ""
    phrase_b = ""
    phrase_h = ""
    while (fin != True):
        lettre = input("Lettre : ")
        if lettre == 'é':
            fin = True
        else:
            dec = ord(lettre)
            print("   Dec : ",dec)
            print("   Bin : ",bin(dec))
            print("   Hex : ",hex(dec))
            phrase = phrase + lettre+" "
            phrase_d = phrase_d + str(dec)+" "            
            phrase_b = phrase_b + str(bin(dec))+" "            
            phrase_h = phrase_h + str(hex(dec))+" "            
    print(phrase)
    print(phrase_d)
    print(phrase_b)
    print(phrase_h)
    
elif trad == 2 :
    fin = False
    print("Traduction Decimal -> ASCII (-1 pour sortir)")
    phrase = ""
    phrase_d = ""
    phrase_b = ""
    phrase_h = ""
    while (fin != True):
        dec = int(input("Valeur : "))
        if dec == -1:
            fin = True
        else:
            print("   char : ",chr(dec))
            print("   Dec : ",dec)
            print("   Bin : ",bin(dec))
            print("   Hex : ",hex(dec))
            phrase = phrase + chr(dec)+" "
            phrase_d = phrase_d + str(dec)+" "            
            phrase_b = phrase_b + str(bin(dec))+" "            
            phrase_h = phrase_h + str(hex(dec))+" "            
    print(phrase)
    print(phrase_d)
    print(phrase_b)
    print(phrase_h)
