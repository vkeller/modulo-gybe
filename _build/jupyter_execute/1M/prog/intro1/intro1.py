#!/usr/bin/env python
# coding: utf-8

# ## Introduction : La tortue
# 
# Nous utilisons le module `turtle` de Python pour cette introduction
# 
# **Objectifs**
# 
# 1. Développement de mon premier programme en Python

# ### Importation du module turtle

# In[1]:


from turtle import *


# Créer une nouvelle tortue que nous nommons `t`
# 
# (Cette opération ouvre une nouvelle fenêtre)

# In[2]:


t = Turtle()


# La tortue est capable de faire plusieurs mouvements. Chaque mouvement est un appel à une fonction :
# 
# - aller en avant de `x`  pixels : `t.forward(x)`
# - aller en arrière de `x` pixels : `t.back(x)`
# - tourner à droite de `x` degrés : `t.right(x)`
# - tourner à gauche de `x` degrés : `t.left(x)`
# 
# On peut changer les caractéristiques du stylo :
# 
# - sa couleur : `t.pencolor('couleur')` par exemple `t.pencolor('red')` en rouge
# - son épaisseur de `e` pixels : `t.pensize(e)`
# 
# Finalement on peut effacer ce que l’on a dessiné avec la fonction `t.clear()`

# ## Dessiner des formes géometriques

# ### Example 1 : Dessiner un triangle
# 
# Le code suivant dessine un triangle équilatéral de côté 100 pixels en bleu avec une épaisseur de 4 pixels

# In[3]:


t.clear()
t.pencolor('blue')
t.pensize(4)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)


# ### Exercice 1
# 
# En utilisant les diverses fonctions de la tortue, dessinez :
# 
# - un carré de 150 pixels de côté en rouge avec une épaisseur de 2
# - un losange vert d’épaisseur 3 avec des angles de 30° et 120°

# ## Nouvelles fonctions de la tortue
# 
# Deux nouvelles fonctions sont ajoutées :
# 
# - lever le stylo : `t.penup()`
# - abaisser le stylo : `t.pendown()`
# 
# Ces deux nouvelles fonctions nous permettent de créer des formes séparées

# ### Example 2
# 
# Dessiner deux triangles équilatéraux de 100 pixels de côté et séparés de 50 pixels :

# In[4]:


t.clear()
t.pencolor('blue')
t.pensize(4)

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.penup()
t.forward(150)
t.pendown()

t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)


# ## Exercice 2
# 
# - Dessinez un carré de 100 pixels de côté et un triangle isocèle de 100 pixels de côté séparés de 30 pixels
# - Dessinez un carré rouge d’épaisseur 3 pixels de 100 pixels de côté et un carré vert d’épaisseur 4 pixels et de 300 pixels de côté séparés par 40 pixels
# 

# In[ ]:




