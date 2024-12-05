from datetime import datetime
import time

while True : 
    horloge = datetime.now()

    heures = horloge.hour
    minutes = horloge.minute
    secondes = horloge.second

    p = 4
    h = [False, False, False, False, False]
    while p >= 0 :
        if heures - 2**p >= 0:
            heures = heures - 2**p
            h[4-p] = True
        p = p - 1

    p = 5
    m = [False, False, False, False, False, False]
    while p >= 0 :
        if minutes - 2**p >= 0:
            minutes = minutes - 2**p
            m[5-p] = True
        p = p - 1

    p = 5
    s = [False, False, False, False, False, False]
    while p >= 0 :
        if secondes - 2**p >= 0:
            secondes = secondes - 2**p
            s[5-p] = True
        p = p - 1

    print(h)
    print(m)
    print(s)
    
    print("SBB -- CFF -- FFS")
    time.sleep(1)


