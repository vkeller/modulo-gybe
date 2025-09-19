choix = input("binaire (1), décimal (2) ou hexadécimal (3) : ")

def hexatobin(hexa):
    hexabin =  {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
    binaire = ""
    for h in hexa:
        binaire = binaire+hexabin[h]
    return binaire

def bintohexa(binaire):
    hexadec =  {"0000":"0","0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D","1110":"E","1111":"F"}
    if len(binaire)%4 != 0:
        toadd = ""
        for i in range(len(binaire)%4):
            toadd = toadd+"0"
        binaire = toadd+binaire
    hexa = ""
    h = ""
    for i in range(len(binaire)):
        h = h + binaire[i]
        if (i+1)%4 == 0 and i != 0:
            hexa = hexa + hexadec[h]
            h = ""
    return hexa

def bintodec(dec):
    dec = 0
    for b in range(len(binaire)):
        if int(binaire[len(binaire)-1-b]) == 1:
            dec = dec + 2**b
    return dec

def dectobin(dec):
    resultat = dec
    binaire = ""
    while resultat != 0:
        binaire = binaire + str(resultat%2)
        resultat = int(resultat/2)

    binaire2 = ""
    for b in range(len(binaire)):
        binaire2 = binaire2+binaire[len(binaire)-1-b]
    return binaire2

if choix == "1" :
    binaire = input("Entrez un nombre entier binaire : ")
    dec = bintodec(binaire)
    hexa = bintohexa(binaire)
    print("Valeur décimale     : ",dec)
    print("Valeur binaire      : ",binaire)
    print("Valeur hexadécimale : ",hexa)

elif choix == "2":
    dec = int(input("Entrez un nombre entier décimal : "))
    binaire = dectobin(dec)
    hexa = bintohexa(binaire)
    print("Valeur décimale     : ",dec)
    print("Valeur binaire      : ",binaire)
    print("Valeur hexadécimale : ",hexa)

elif choix == "3":
    hexa = input("Entrez un nombre entier hexadécimal : ")
    binaire = hexatobin(hexa)
    dec = bintodec(binaire)
    print("Valeur décimale     : ",dec)
    print("Valeur binaire      : ",binaire)
    print("Valeur hexadécimale : ",hexa)
    
    
else :
    print("Votre choix",choix,"n'est pas possible (1, 2 ou 3)")
