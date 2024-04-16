def est_vide(pile):
    vide = False
    if len(pile) == 0:
        vide = True
    return vide

def empiler(pile, element):
    pile.append(element)

def depiler(pile):
    long = len(pile)
    element = pile[long-1]
    pile.pop()
    return element

def deplacer(pile1, pile2):
    element = depiler(pile1)
    pile2.append(element)

def afficher(pile):
    if est_vide(pile) == False:
        for i in range(len(pile)-1,-1,-1):
            print(pile[i]*"-")
    else:
        print("Attention, la pile est vide")

pilier1 = []
pilier2 = []
pilier3 = []

for i in range(6,0,-1):
    empiler(pilier1,i)

afficher(pilier1)
print("========================")
deplacer(pilier1,pilier2)
deplacer(pilier1,pilier3)
deplacer(pilier2,pilier3)
afficher(pilier3)

print("========================")

