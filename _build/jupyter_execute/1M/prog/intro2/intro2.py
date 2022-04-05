#!/usr/bin/env python
# coding: utf-8

# # Introduction : les fonctions

# **Objectifs** : introduire le concept de fonction. Ecrire sa première fonction. 

# Peut-être avez-vous remarqué que nous avons plusieurs fois effectué des opérations très proches et qui variaient peu :
# 
# 1. dessiner un carré
# 1. dessiner un carré rouge/vert/bleu
# 1. dessiner un carré rouge/vert/bleu de 100/200/300 de côté
# 1. dessiner un carré rouge/vert/bleu de 100/200/300 de côté et d’épaisseur 3/4/5 pixels
# 
# Peut-on s’économiser du temps (et de l’argent) ? Parce qu’un carré, c’est toujours 4 côtés de longueur identique à angle droit. La couleur, la longueur, l’épaisseur, ne sont que des caractéristiques de la même forme. 
# 
# La réponse est **OUI**. Cela s’appelle **une fonction**. 

# ## Fonction
# 
# Les fonctions sont très utiles pour réaliser plusieurs fois les mêmes opérations au sein d'un programme informatique. Elles rendent également le code plus lisible et plus clair en le fractionnant en blocs logiques (modules).

# ### Définition
# 
# Pour définir une fonction, il s'agit de respecter la signature suivante. On commence par le mot-clef `def` suivi du nom de la fonction (sans accents) puis de deux points `:`. Le contenu de la fonction (les opérations qui seront répétées) doivent **impérativement** être écrites avec une indentation sur **la droite**.
# 
# Par exemple :
# 
# ```
# def nomDeLaFonction(arg):
#    operation1
#    operation2
#    etc..
# ```

# ### Fonction sans argument 
# 
# Une fonction sans argument qui écrit `Bonjour` a la forme suivante :

# In[1]:


def hello():
    print("Bonjour !")


# Que l'on peut appeler dans le **programme principal**

# In[2]:


hello()


# On peut l'appeler plusieurs fois dans le programme principal

# In[3]:


hello()
hello()
hello()


# ### Fonction avec argument
# 
# Une fonction peut avoir un ou des arguments séparés par une virgule `,`. Ces arguments peuvent ensuite être utilisés dans les opérations effectuées dans le corps de la fonction.
# 
# Par exemple une fonction qui élève un nombre `x` au cube a la forme suivante ;

# In[4]:


def cube(x):
    return x*x*x


# On peut ensuite appeler cette fonction dans le **programme principal**

# In[5]:


print(cube(4))


# ## Dessiner des carrés avec la tortue
# 
# Dans l’exemple du carré, nous avons 3 caractéristiques :
# 
# - la couleur
# - la longueur d’un côté
# - l’épaisseur du trait
# 
# Une fonction qui dessine un carré s'écrit :

# In[6]:


from turtle import *


# In[7]:


def carre():
    t.pencolor('red')
    t.pensize(3)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)    


# que l'on appelle dans le programme principal :

# In[8]:


t = Turtle()
carre()


# Pour changer la taille, la couleur et l'épaisseur du trait on peut passer les paramètres en argument de la fonction :

# In[9]:


def carre2(longueur, couleur, epaisseur) :
    t.pencolor(couleur)
    t.pensize(epaisseur)
    t.forward(longueur)
    t.left(90)
    t.forward(longueur)
    t.left(90)
    t.forward(longueur)
    t.left(90)
    t.forward(longueur)
    t.left(90)        


# que l'on appelle ensuite dans le programme principal :

# In[10]:


carre2(150,'blue',4)


# ## Exercice 1
# 
# Ecrivez une fonction `losange` qui dessine un losange (angle de 60°) et qui prend les paramètres suivants :
# 
# - la couleur
# - la longueur du côté du l
# 

# ## Exercice 2 (appel d'une fonction dans une fonction)
# 
# A l'aide des fonctions `penup()` et `pendown()` qui permettent de lever et d'abaisser le crayon, écrivez une fonction qui dessine une maison.
# 
# Il s'agit d'écrire trois fonctions :
# 
# 1. `triangle()` qui dessine le toit
# 1. `carre()`qui dessine la maison
# 1. `maison()` qui appelle les deux
