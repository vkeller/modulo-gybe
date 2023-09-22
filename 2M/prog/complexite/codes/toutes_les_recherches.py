import random

def random_non_tire(already,bmin,bmax):
    ret = 0
    nontire = False
    while nontire != True :
        aleat = random.randint(bmin,bmax)
        tire = False
        for i in range(len(already)):
            if already[i] == aleat :
                tire = True
        if tire == False:
            nontire = True
    return aleat

def recherche_lineaire(_atrouver):
    N = 0
    nombre = 0
    trouve = False
    while (trouve!=True):
        if (nombre==_atrouver):
            trouve=True
        nombre = nombre + 1
        N = N + 1
    return N

def recherche_aleatoire_sans(_atrouver,_borneInf,_borneSup):
    N = 0
    trouve = False
    deja_tire = []
    while (trouve!=True):
        aleatoire = random_non_tire(deja_tire,_borneInf,_borneSup)
        if (aleatoire == _atrouver) :
            trouve=True
        N = N + 1
        deja_tire.append(aleatoire)
    return N

def recherche_aleatoire_avec(_atrouver,_borneInf, _borneSup):
    N = 0
    trouve = False
    while (trouve!=True):
        aleatoire = random.randint(_borneInf,_borneSup)
        if (aleatoire == atrouver) :
            trouve=True
        N = N + 1
    return N

def recherche_dichotomique(_atrouver,_borneInf,_borneSup):
    N = 0
    trouve = False
    bmax = _borneSup
    bmin = _borneInf
    while (trouve!=True):
        moitie = int((bmax+bmin)/2)
        if (moitie == _atrouver) :
            trouve=True
        elif (moitie > _atrouver) :
            bmax = moitie
        elif (moitie < _atrouver) :
            bmin = moitie
        N = N + 1
    return N

    
borneInf = 0
borneSup = 100000
atrouver = random.randint(borneInf,borneSup)

print("\t Recherche linéaire       : "+str(recherche_lineaire(atrouver)))
print("\t Recherche aleatoire avec : "+str(recherche_aleatoire_avec(atrouver,borneInf,borneSup)))
print("\t Recherche aleatoire sans : "+str(recherche_aleatoire_sans(atrouver,borneInf,borneSup)))
print("\t Recherche dichotomique   : "+str(recherche_dichotomique(atrouver,borneInf,borneSup)))


#for i in range(1,100,10):
#    borneInf = 100
#    borneSup = i
#    print(str(i)+"Recherche de "+str(atrouver))
#    print("\t Recherche linéaire       : "+str(recherche_lineaire(atrouver)))
#    print("\t Recherche aleatoire avec : "+str(recherche_aleatoire_avec(atrouver,borneInf,borneSup)))
#    print("\t Recherche aleatoire sans : "+str(recherche_aleatoire_sans(atrouver,borneInf,borneSup)))
#    print("\t Recherche dichotomique   : "+str(recherche_dichotomique(atrouver,borneInf,borneSup)))
