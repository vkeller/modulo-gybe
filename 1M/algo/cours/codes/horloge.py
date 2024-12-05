heures    = int(input("heure    : "))
minutes   = int(input("minutes  : "))
secondes  = int(input("secondes : "))
p = 4
h = [False, False, False, False, False]
while p >= 0 :
    if heures - 2**p >= 0:
        print("Lumière",p,"ON")
        heures = heures - 2**p
        h[4-p] = True
    else:
        print("Lumière",p,"OFF")
    p = p - 1

p = 5
m = [False, False, False, False, False, False]
while p >= 0 :
    if minutes - 2**p >= 0:
        print("Lumière",p,"ON")
        minutes = minutes - 2**p
        m[5-p] = True
    else:
        print("Lumière",p,"OFF")
    p = p - 1

p = 5
s = [False, False, False, False, False, False]
while p >= 0 :
    if secondes - 2**p >= 0:
        print("Lumière",p,"ON")
        secondes = secondes - 2**p
        s[5-p] = True
    else:
        print("Lumière",p,"OFF")
    p = p - 1

print(h)
print(m)
print(s)

