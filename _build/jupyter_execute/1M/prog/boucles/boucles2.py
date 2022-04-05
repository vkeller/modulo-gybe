#!/usr/bin/env python
# coding: utf-8

# # Dessiner des spirales
# 
# **Objectif :** approfondir le concept de fonction et de boucles
# 
# ## Définition d’une spirales
# 
# Une spirale est un objet formé de segments dont la longueur augmente à chaque itération
# 
# 
# ## Exercice 1
# 
# Ecrivez un programme qui dessine une spirale qui commence avec une longueur de segment de 2 et qui augmente chaque fois de 1. L’angle choisi est de 30
# 
# ## Exercice 2
# 
# Modifiez votre programme en écrivant une fonction spirale() qui reprend chaque étape du programme principal
# 
# ## Exercice 3
# 
# Réécrivez votre fonction spirale() avec une boucle jusqu’à 20
# 
# ## Exercice 4
# 
# Ecrivez une fonction spirale(ns,angle) avec deux paramètres : le nombre de segments et l’angle.
# 
# ## Exercice 5 (a step forward)
# 
# Est-il possible d’améliorer la courbure de la spirale et donc d’affiner le segment en arc de cercle ?
# 
# **Indications :**
# 
# Il s’agit de réfléchir au dessin de l’arc de spirale (avec une boucle)
# 
# La fonction origine() suivante permet de faire revenir la tortue à l’origine :

# In[1]:


def origine():
    t.penup()
    t.goto(0,0)
    t.setheading(0)
    t.pendown()


# In[ ]:




