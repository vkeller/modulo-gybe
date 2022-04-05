#!/usr/bin/env python
# coding: utf-8

# # Les boucles : dessins animés
# 
# **Objectifs** Utiliser la tortue pour créer un dessin animé.
# 
# ## Définition : dessin animé
# 
# Film réalisé à partir d’une série de dessins qui décomposent les mouvements des personnages et qui, projetés, donnent l’impression d’un mouvement continu.
# 
# ## Histoire de l'animation et des films
# 
# - Première photographie : 1827 «Point de vue du Gras» Nicéphore Nièpce, héliographie («écriture par le soleil») prise depuis le premier étage de son atelier.
# - Premier film («kinétographe») 1895 : «La sortie de l’usine Lumières à Lyon», les Frères Lumières
# - Format argentique «standard» : 35 millimètres. 24 images par seconde. Sons synchronisés.
# - Premiers dessins animés : 1892, «Pantomimes lumineuses» d’Emile Reynaud.
# - Premiers dessins animés informatisés : 1980. Animation vectorielle, images de synthèse, animation 2D, animation 3D. 

# ## Python pour les dessins animés
# 
# Nous allons procéder en deux étapes :
# 
# 1. définition du dessin animé (CE QUE NOUS VOULONS COMME RESULTAT)
# 1. construction des sous-éléments de l’animation

# ## Notre dessin animé
# 
# Notre dessin animé sera simple. Voici l’algorithme :
# 
# 1. on dessine un carré de 80 pixels de côté,
# 1. on attend un moment
# 1. on l’efface, 
# 1. on déplace la tortue à droite de 2 pixels
# 1. on dessine un carré de 80 pixels de côté
# 1. et on recommence...
# 
# l’impression sera que le carré glisse vers la droite.

# ## Exercice 1
# 
# Construction des sous-éléments du dessin animé.
# 
# Définissez deux fonctions :
# 
# 1. `carre()` qui dessine un carré de 80 pixels de côté
# 1. `attendEtAvance()` qui attend 0.5 secondes et avance de 2 pixels
# 
# Quelques fonctions utiles pour la fonction attendreEtAvancer() :
# 
# `t.penup()` : pour lever le crayon
# `t.pendown()` : pour abaisser le crayon
# `t.clear()` : pour effacer ce qui a été dessiné
# 
# Une fonction importante pour «dormir» une seconde :
# 
# ```
# from time import *
# sleep(1)
# ```

# ## Exercice 2
# 
# Ecrivez un programme qui anime le carré en faisant appel aux diverses fonctions crées plus haut
# 
# **Remarque:** on peut accélérer la tortue avec la **méthode** (qui est une fonction appliquée à un objet) `t.speed(vitesse)` où l'argument `vitesse` est un chiffre très élevé (par exemple 500). 

# ## Exercice 3 (avancé en utilisant une boucle)
# 
# Une boucle ce n'est rien d'autre qu'une itération de plusieurs opérations. On la déclare de la façon suivante :
# 
# ```
# for i in range(10) :
#    operation 1
#    operation 2
#    etc..
# ```
# 
# est une boucle qui fera les opérations indentées à droite 10 fois. 

# In[ ]:




