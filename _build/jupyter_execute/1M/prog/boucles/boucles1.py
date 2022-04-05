#!/usr/bin/env python
# coding: utf-8

# # Boucles
# 
# **Objectif** Introduction du concept de boucles dans un programme

# ## Définition
# 
# Lorsque nous devons répéter plusieurs fois la ou les mêmes opérations, il est utile de le dire à l’ordinateur. C’est le concept de boucle.

# ## Example : dessiner un triangle équilatéral
# 
# La fonction pour dessiner un triangle équilatéral peut s'écrire ainsi :

# In[1]:


def triangle():
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)


# fonction que l'on peut ensuite appeler dans le programme principal :

# In[2]:


from turtle import *
t = Turtle()
triangle()


# On observe qu’on a 3 fois deux instructions identiques :
# 
# ```
# 	t.forward(100)
# 	t.left(120)
# ```

# On peut transformer ces trois instructions identiques en une boucle qui les appelerait les trois à la suite :
# 
# ```
# pour i = 1, 2, 3 faire:
#    t.forward(100)
#    t.left(120)
# ```
# 
# En Python, une boucle s'écrit en utilisant le mot-clef `for`, suivi d'une variable nommée **itérateur**, par convention on la nomme `i`, puis des deux mot-clefs `in range(x)` où la valeur de `x` est la portée de l'intervalle.
# 
# Ainsi la fonction pour dessiner un triangle devient :

# In[3]:


def triangle2():
    for i in range(3):
        t.forward(100)
        t.left(120)


# que l'on peut ensuite appeler dans le programme principal :

# In[4]:


triangle2()


# ## Exercice 1
# 
# Ecrivez deux fonctions `triangle()` qui dessine un triangle équilatéral de côté 100 et `carre()` qui dessine un carré de côté 100

# ## Observation
# 
# On observe que :
# 
# - Triangle : 3 fois avancer et tourner de 120° (3 x 90° = 360°)
# - Carré : 4 fois avancer et tourner de 90° (4 x 90° = 360°)
# 
# Est-il possible de généraliser la fonction pour dessiner n'importe quel polygone de côté 100 avec une boucle ?

# ## Exercice 2
# 
# Ecrivez une fonction `polygone` qui prend en paramètre le nombre de côté du polygone et qui le génère

# ## Exercice 3
# 
# De quelle forme géométriqu
