
mere = 30
for f in range(1,11):
    print("le fils a "+str(f)+" ans")
    for j in range(15):
        mere = 40
        fils = f
        for i in range(90):
            if (mere/fils==j):
                print("\t"+str(j)+" x l'âge de la mère")
                print("\t"+"mere = "+str(mere))
                print("\t"+"fils = "+str(fils))        
            mere += 1
            fils += 1
