import urllib.request
import json
import time
from datetime import datetime

# Zone du gymnase (latitude et longitude)
LAT_MIN = 0
LAT_MAX = 100
LON_MIN = 0
LON_MAX = 100

#URL = "http://localhost:8080/data/aircraft.json"
URL = "file:///run/dump1090-mutability/aircraft.json"

def est_dans_zone(lat, lon):
    return LAT_MIN <= lat <= LAT_MAX and LON_MIN <= lon <= LON_MAX

def collecter():
    try:
        with urllib.request.urlopen(URL) as response:
            data = json.loads(response.read())
        avions = data.get("aircraft", [])

        avions_filtrés = []
        for avion in avions:
            lat = avion.get("lat")
            lon = avion.get("lon")
            if lat is not None and lon is not None and est_dans_zone(lat, lon):
                vitessekm = avion.get("speed",0)
                vitessekm = int(vitessekm*1.609344)
                altitudem = avion.get("altitude",0)
                altitudem = int(altitudem*0.3048)
                avions_filtrés.append({
                    "flight": avion.get("flight", "").strip(),
                    "lat": lat,
                    "lon": lon,
                    "altitude": altitudem,
                    "speed": vitessekm,
                    "timestamp": datetime.now().isoformat()
                })

        # Sauvegarde dans un fichier JSON
        with open("/var/www/html/adsb/avions.json", "w") as f:
            json.dump(avions_filtrés, f, indent=4)

        print(f"{len(avions_filtrés)} avions sauvegardés.")
    except Exception as e:
        print("Erreur :", e)

if __name__ == "__main__":
    while True:
        collecter()
        time.sleep(2)  # Répéter toutes les 60 secondes
