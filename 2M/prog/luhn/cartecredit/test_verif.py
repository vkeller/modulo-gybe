carte2 = [4,3,9,6,8,3,7,4,1,2,0,4,2,7,5,5]
carte = carte2
limite = len(carte)
somme = 0
for i in range(limite):
    if (i%2) == 0:
        e = (carte[i]*2)
        if e>9 :
            e = e-9
        print(((carte[i]*2)%9),e)
        somme += e
    else:
        somme += carte[i]
