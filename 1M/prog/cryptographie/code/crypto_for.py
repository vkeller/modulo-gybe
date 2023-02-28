# ==============================================
# Cryptographie
#
# Vincent Keller, Gymnase de Beaulieu (c) 2023
# ==============================================

import random

phrase_a_1 = "Arise, you have nothing to lose but your barbed wire fences!"
phrase_a_2 = "If privacy is outlawed, only outlaws will have privacy"
phrase_a_3 = "Show me a person who has nothing to hide, and I’ll show you a person who is either exceedingly dull or an exhibitionist"
phrase_a_4 = "One of the best ways to achieve justice is to expose injustice"
phrase_a_5 = "I am a future-hacker ; I am trying to get root access to the futur. I want to ride its system of thought"
phrase_a_6 = "Girls need modems"

phrase_f_1 = "La valeur d’un trésor réside dans son secret"
phrase_f_2 = "La cryptographie est la forme la plus aboutie de l’action directe non-violente"
phrase_f_3 = "L’argent c’est du temps, sauf si vous n’avez pas l’un ou l’autre"
phrase_f_4 = "Un téléphone portable émet des signaux de localisation. Lorsqu’on a un téléphone portable, le réseau sait toujours où l’on se trouve"
phrase_f_5 = "Si vous possédez une bibliothèque et un jardin, vous avez tout ce qu’il vous faut"
phrase_f_6 = "Combien de vous n’ont pas violé de loi ce mois-ci ?"
phrase_f_7 = "Si vous surveillez tout le monde, vous ne surveillez personne"

dataset_a = [phrase_a_1,phrase_a_2,phrase_a_3,phrase_a_4,phrase_a_5,phrase_a_6]
dataset_f = [phrase_f_1,phrase_f_2,phrase_f_3,phrase_f_4,phrase_f_5,phrase_f_6,phrase_f_7]

# Fonction permettant de chiffrer un texte en clair
# Argument 1 : le texte clair
# Argument 2 : la clef de chiffrage
# Retour     : le texte chiffré
def chiffre(texte_clair,clef):
    texte_chiffre = ''
    # la variable pos contient l'index (la position) dans le texte clair
    pos = 0
    # la variable dec contient l'incrément négatif lorsque la longueur du texte clair est atteinte
    dec = 0
    # la variable pos_c contient l'index (la position) dans le texte chiffré
    pos_c = 0
    # la variable l contient la longueur du texte clair
    l = len(texte_clair)
    for pos in range(l):
        if (pos_c > l-1):
            dec += 1
            pos_c = dec
        texte_chiffre += texte_clair[pos_c]
        pos_c = pos_c + clef
    return texte_chiffre    

# Fonction permettant de déchiffrer un texte crypté
# Argument 1 : le texte crypté
# Argument 2 : la clef de chiffrage
# Retour     : le texte déchiffré
def dechiffre(texte_chiffre,clef):
    # la variable l contient la longueur du texte chiffré
    l = len(texte_chiffre)
    # la variable pos continent l'index (la position) dans le texte chiffré
    pos = 0
    # la varibale pos_c contient l'index (la position) dans le texte clair
    pos_c = 0
    # la variable dec contient la valeur de l'incrément positif
    dec = 0
    # la variable ret est une liste de longueur l qui est vide et que l'on va remplir avec les lettre du texte chiffré
    ret = ['' for _ in range(l)]
    for pos in range(l):
        if (pos_c > l-1):
            dec += 1
            pos_c = dec
        ret[pos_c] = texte_chiffre[pos]
        pos_c = pos_c + clef
    # on retourne une chaîne de caractères (''.join(ret) retourne la transformation de la liste en chaîne de caractères)
    return ''.join(ret)

# Fonction permettant de retourner la langue d'un texte donné en paramètre
# sur la base d'une analyse de certains mots clefs
# La liste des mots clefs est basée sur les classements internationaux (comme COCA)
# Argument 1 : le texte clair
# Retour     : la langue possible
def analyse_langue(texte):
    mots_clefs_f = ['le','la','les','un','une','de','des','il','elle','et','non','est','on','vous','nous','se','pas','leur']
    mots_clefs_a = ['the','be','to','of','and','in','that','have','it','for','not','is','if']
    retour = ['',0]
    l = len(texte)
    nbr_f = 0
    nbr_a = 0
    for mot_clef in mots_clefs_f:
        if (texte.find(mot_clef) != -1):
            nbr_f += 1

    for mot_clef in mots_clefs_a:
        if (texte.find(mot_clef) != -1):
            nbr_a += 1

    if nbr_f == 0 and nbr_a == 0:
        retour = ['NULL',0]
    elif nbr_f > nbr_a:
        retour = ['FRA ',nbr_f]
    else:
        retour = ['ENG ',nbr_a]

    return retour

texte_clair = phrase_f_1
texte_chiffre = ''
texte_dechiffre = ''

# Création des phrases chiffrées aléatoirement
# Et déchiffrement SANS élagage
#for phrase in dataset_a:
#    longueur = len(phrase)
#    clef = random.randint(3,int(longueur/2))
#    texte_chiffre = chiffre(phrase,clef)
#    print('[Cyphered] '+str(clef)+"   : "+texte_chiffre)
#    for clef in range(1,longueur):
#        texte_dechiffre = dechiffre(texte_chiffre,clef)
#        print('  [ANALYSED '+str(clef)+']   : '+texte_dechiffre)



# Création des phrases chiffrées aléatoirement
# Et déchiffrement avec élagage

#for phrase in dataset_f:
#    longueur = len(phrase)
#    clef = random.randint(3,int(longueur/2))
#    texte_chiffre = chiffre(phrase,clef)
#    print('[Cyphered] '+str(clef)+"   : "+texte_chiffre)
#    probables = []
#    score = 0
#    for clef in range(1,longueur):
#        texte_dechiffre = dechiffre(texte_chiffre,clef)
#        analyse = analyse_langue(texte_dechiffre)
#        if analyse[1] >= score:
#            score = analyse[1]
#            probables.append([texte_dechiffre,analyse,clef])
#    for probable in probables:
#        print('  [ANALYSED '+probable[1][0]+' score ',probable[1][1],' clef ',probable[2],']   : '+probable[0])
#    print('  Taux de rejet = '+str(100-len(probables)/longueur*100)+' %')


#phrase = "La cryptographie, la science de l écriture de codes et de chiffrements pour une communication sécurisée, est l un des éléments principaux ayant rendu possible l’invention des crypto-monnaies et des blockchains modernes. Les techniques cryptographiques utilisées aujourd hui sont cependant le fruit d une longue histoire de développement. Depuis l Antiquité, la cryptographie permet de transmettre des informations de manière sécurisée. Voici l’histoire fascinante de la cryptographie qui a conduit aux méthodes avancées et sophistiquées utilisées pour le cryptage numérique moderne.   Les racines anciennes de la cryptographie  On sait que les techniques cryptographiques primitives existaient dans l Antiquité et, à un certain degré, la plupart des civilisations anciennes semblent avoir eu recours à la cryptographie. Le remplacement de symbole, la forme la plus élémentaire de cryptographie, apparaît à la fois dans les écrits égyptiens antiques et mésopotamiens. Le plus ancien exemple connu de ce type de cryptographie a été trouvé dans la tombe d un noble égyptien nommé Khnumhotep II, qui vivait il y a environ 3 900 ans.  Le remplacement de symboles dans l’inscription de Knhumhotep n’a pas pour objectif de dissimuler des informations, mais de renforcer leur attrait linguistique. Le premier exemple connu de cryptographie utilisée pour protéger des informations confidentielles date de 3 500 ans environ. Un scribe mésopotamien recourait à la cryptographie pour dissimuler une formule de glaçure de poterie, utilisée sur des tablettes d argile.  Par la suite, la cryptographie a largement été utilisée pour protéger des informations militaires importantes, c’est une utilisation encore répandue à ce jour. Dans la cité grecque de Sparte, les messages étaient cryptés en étant rédigés sur un parchemin posé sur un cylindre d une taille particulière, rendant le message indéchiffrable jusqu à ce qu il soit enroulé autour d un cylindre similaire par le destinataire. De même, on sait que des espions de l’Inde antique utilisaient des messages codés dès le IIe siècle av JC..  La cryptographie la plus avancée du monde antique a peut-être été crée par les Romains. Un exemple marquant de la cryptographie romaine, connu sous le nom de chiffrement par décalage, consistait à changer les lettres du message que l’on voulait crypter en les remplaçant par des lettres décalées d’un certain nombre de places dans l’ordre de l’alphabet latin. Le destinataire pouvait décoder avec succès le message, par ailleurs illisible, s’il connaissait le système et le décalage à effectuer.   Évolution au Moyen Âge et à la Renaissance  Au cours du Moyen Âge, la cryptographie est devenue de plus en plus importante, mais les codes de substitution, dont le chiffrement par décalage est un exemple, subsitèrent en tant que norme. La cryptanalyse, la science par laquelle les messages et les codes sont déchiffrés, a commencé à rattraper la science encore relativement primitive de la cryptographie. Al-Kindi, un mathématicien arabe réputé, mis au point une technique connue sous le nom d’analyse de fréquence vers 800 après J.-C. qui rendait les algorithmes de substitution vulnérables au déchiffrement. Pour la première fois, les personnes qui tentaient de déchiffrer des messages codés eurent accès à une méthode systématique, ce qui rendit nécessaire la progression de la cryptographie pour qu’elle reste efficace.  En 1465, Leone Alberti développa le poly alphabétique, considéré comme la solution contre la technique d analyse de fréquence d Al-Kindi. Dans un chiffre polyalphabétique, un message est codé en utilisant deux alphabets distincts. L un est l alphabet dans lequel le message original est écrit, tandis que le second est un alphabet entièrement différent dans lequel le message apparaît après avoir été codé. Combinés aux chiffrements de substitution traditionnels, les chiffrements polyalphabétiques ont considérablement augmenté la sécurité des informations codées. À moins qu un lecteur ne connaisse l alphabet dans lequel le message avait été écrit à l origine, la technique d analyse de fréquence était inutile.  De nouvelles méthodes de codage de l’information ont également été mises au point à la Renaissance, notamment une méthode populaire de codage binaire, inventée par le célèbre intellectuel Sir Francis Bacon en 1623.   Les progrès des siècles plus récents  La science de la cryptographie a continué à progresser progressivement au cours des siècles. Une avancée majeure en matière de cryptographie a été décrite, bien que peut-être jamais construite, par Thomas Jefferson dans les années 1790. Son invention, connue sous le nom de roue de chiffrement, consiste en 36 anneaux de lettres sur des roues mobiles qui peuvent être utilisés pour réaliser un codage complexe. Ce concept était tellement avancé qu il servit de base à la cryptographie militaire américaine jusqu à la fin de la Seconde Guerre mondiale.  La Seconde Guerre mondiale mit également en valeur le parfait exemple de la cryptographie analogique, connue sous le nom de machine Enigma. Comme le chiffrement de roue, cet appareil, utilisé par les puissances de l Axe, utilisait des roues rotatives pour coder un message, ce qui rendait la lecture pratiquement impossible sans une autre machine Enigma. Les premières technologies informatiques ont finalement été utilisées pour aider à casser le cryptage Enigma, et le déchiffrement réussi des messages Enigma est toujours considéré comme un élément essentiel de la victoire finale des Alliés.   La cryptographie à l ère de l informatique  Avec l essor de l’informatique, la cryptographie est devenue beaucoup plus avancée qu elle ne l était à l époque analogique. Le cryptage mathématique sur 128 bits, beaucoup plus puissant que tout cryptage antique ou médiéval, est désormais la norme pour de nombreux périphériques et systèmes informatiques sensibles. À partir de 1990, des informaticiens ont mit au point une toute nouvelle forme de cryptographie, appelée cryptographie quantique, dans l espoir de rehausser le niveau de protection offert par le cryptage moderne.  Plus récemment, des techniques cryptographiques ont également été utilisées pour rendre les crypto-monnaies possibles. Les crypto-monnaies utilisent plusieurs techniques cryptographiques avancées, notamment les fonctions de hachage, la cryptographie à clé publique et les signatures numériques. Ces techniques sont principalement utilisées pour assurer la sécurité des données stockées sur les blockchains et pour authentifier les transactions. Une forme de cryptographie spécialisée, appelée algorithme de signature numérique à courbe elliptique (ECDSA), sous-tend Bitcoin et d autres systèmes de crypto-monnaie afin de renforcer la sécurité et de garantir que les fonds ne peuvent être utilisés que par leurs propriétaires véritables.  La cryptographie a parcouru un long chemin au cours des 4 000 dernières années et cela ne devrait pas s arrêter de si tôt. Tant que les données sensibles nécessitent une protection, la cryptographie continuera de progresser. Bien que les systèmes cryptographiques utilisés dans les blockchains de crypto-monnaies représentent aujourd hui l une des formes les plus avancées de cette science, ils font également partie d une histoire qui remonte à travers les âges et constitue une grande partie de l histoire de l’homme."
#phrase = "La cryptographie, la science de l écriture de codes et de chiffrements pour une communication sécurisée, est l un des éléments principaux ayant rendu possible l’invention des crypto-monnaies et des blockchains modernes. Les techniques cryptographiques utilisées aujourd hui sont cependant le fruit d une longue histoire de développement. Depuis l Antiquité, la cryptographie permet de transmettre des informations de manière sécurisée. Voici l’histoire fascinante de la cryptographie qui a conduit aux méthodes avancées et sophistiquées utilisées pour le cryptage numérique moderne.   Les racines anciennes de la cryptographie  On sait que les techniques cryptographiques primitives existaient dans l Antiquité et, à un certain degré, la plupart des civilisations anciennes semblent avoir eu recours à la cryptographie. Le remplacement de symbole, la forme la plus élémentaire de cryptographie, apparaît à la fois dans les écrits égyptiens antiques et mésopotamiens. Le plus ancien exemple connu de ce type de cryptographie a été trouvé dans la tombe d un noble égyptien nommé Khnumhotep II, qui vivait il y a environ 3 900 ans.  Le remplacement de symboles dans l’inscription de Knhumhotep n’a pas pour objectif de dissimuler des informations, mais de renforcer leur attrait linguistique. Le premier exemple connu de cryptographie utilisée pour protéger des informations confidentielles date de 3 500 ans environ. Un scribe mésopotamien recourait à la cryptographie pour dissimuler une formule de glaçure de poterie, utilisée sur des tablettes d argile."
#longueur = len(phrase)
#clef = random.randint(3,int(longueur/2))
#texte_chiffre = chiffre(phrase,clef)
#print('[Cyphered] '+str(clef)+"   : "+texte_chiffre)
#probables = []
#score = 0
#for clef in range(1,longueur):
#    texte_dechiffre = dechiffre(texte_chiffre,clef)
#    analyse = analyse_langue(texte_dechiffre)
#    if analyse[1] >= score:
#        score = analyse[1]
#        probables.append([texte_dechiffre,analyse,clef])
#for probable in probables:
#    print('  [ANALYSED '+probable[1][0]+' score ',probable[1][1],' clef ',probable[2],']   : '+probable[0])
#print('  Taux de rejet = '+str(100-len(probables)/longueur*100)+' %')



#for phrase in dataset_a:
#    print(phrase)
#    langue = analyse_langue(phrase)
#    print(langue)

#for s in range(3,20):
#    texte_chiffre = chiffre(texte_clair,s)
#    print('[C] '+str(s)+"   : "+texte_chiffre)
#    texte_dechiffre = dechiffre(texte_chiffre,s)
#    print('[D] '+str(s)+"   : "+texte_dechiffre)

# Longue phrase (clef = 652)
# La cryptographie, la science de l écriture de codes et de chiffrements pour une communication sécurisée, est l un des éléments principaux ayant rendu possible l’invention des crypto-monnaies et des blockchains modernes. Les techniques cryptographiques utilisées aujourd hui sont cependant le fruit d une longue histoire de développement. Depuis l Antiquité, la cryptographie permet de transmettre des informations de manière sécurisée. Voici l’histoire fascinante de la cryptographie qui a conduit aux méthodes avancées et sophistiquées utilisées pour le cryptage numérique moderne.   Les racines anciennes de la cryptographie  On sait que les techniques cryptographiques primitives existaient dans l Antiquité et, à un certain degré, la plupart des civilisations anciennes semblent avoir eu recours à la cryptographie. Le remplacement de symbole, la forme la plus élémentaire de cryptographie, apparaît à la fois dans les écrits égyptiens antiques et mésopotamiens. Le plus ancien exemple connu de ce type de cryptographie a été trouvé dans la tombe d un noble égyptien nommé Khnumhotep II, qui vivait il y a environ 3 900 ans.  Le remplacement de symboles dans l’inscription de Knhumhotep n’a pas pour objectif de dissimuler des informations, mais de renforcer leur attrait linguistique. Le premier exemple connu de cryptographie utilisée pour protéger des informations confidentielles date de 3 500 ans environ. Un scribe mésopotamien recourait à la cryptographie pour dissimuler une formule de glaçure de poterie, utilisée sur des tablettes d argile.
