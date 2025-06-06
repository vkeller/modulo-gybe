import pyModeS as pms

# 🔢 Exemple ssage ADS-B hexadécimal
message = "8DA9C3F2201A0A3F8B096527B6F0"  # à remplacer par un message réel
message2 = "8D4840D6202CC371C32CE0576098"
message3 = "8DAE02C85864A5F5DD4975A1A3F5"
message = message2
print("Message ADS-B reçu :", message)

# 1️⃣ Adresse ICAO de l’avion (code unique de 24 bits)
icao = pms.common.icao(message)
print("Adresse ICAO :", icao, "identifiant unique de l'avion")

# 2️⃣ Type de message : cela détermine le contenu (position, vitesse, etc.)
tc = pms.adsb.typecode(message)
print("Typecode :", tc)

# 3️⃣ Décodage selon le type de message
if 1 <= tc <= 4:
    # ✈️ Identification de vol (callsign)
    callsign = pms.adsb.callsign(message)
    print("Appel radio (Callsign) :", callsign)

elif 9 <= tc <= 18:
    # 📍 Position (partielle) et altitude
    altitude = pms.adsb.altitude(message)
    cpr_format = pms.adsb.cpr_format(message)
    print("Altitude :", altitude, "ft")
    print("Format CPR :", "pair" if cpr_format == 0 else "impair")
    print("⚠️ Pour obtenir la position complète, il faut un second message (CPR pair + impair)")

elif 19 <= tc <= 22:
    # 🚀 Vitesse et cap
    speed, heading, vrate = pms.adsb.velocity(message)
    print("Vitesse sol :", speed, "nœuds")
    print("Cap :", heading, "°")
    print("Taux de montée/descente :", vrate, "ft/min")

else:
    print("Message non pris en charge dans cette démo simple.")