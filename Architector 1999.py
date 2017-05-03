import random
from tkinter import *

#Création d'un première liste contenant un nombre de pièces aléatoire
#Chaque pièces est défini par deux points de coordonnées (x,y)
#Les coordonnées sont misent en "bazar", elles ne sont pas oraganisées

def pieces():
    for i in range(0,nb_pieces,1):
        x=random.randint(2,int(largeur/2))
        y=random.randint(2,int(longueur/2))
        liste_bazar.extend([x,y])
    print(liste_bazar)


#On cherche à poser les pièces de la plus grande à la plus petite
#En effet ainsi les pièces les plus importantes sont présentes
#On range donc les coordonnées dans une liste "rangée"

def tri():
    c=0
    k=0
    for y in range (0,len(liste_bazar),2):
        c=0
        for x in range (0,len(liste_bazar),2):
            if liste_bazar[x]*liste_bazar[x+1]>c:
                c=liste_bazar[x]*liste_bazar[x+1]
                k=x
            else:
                c=c
        liste_rangée.append(liste_bazar[k])
        liste_rangée.append(liste_bazar[k+1])
        liste_bazar[k],liste_bazar[k+1]=0,0
    print(liste_rangée)

#Maintenant que nous avons toutes les coordonnées rangée,
#On vérifie que celle-ci ne se superposent pas ou ne sont pas l'une dans l'autre
#On crée donc la fonction "check" qui rangerais les coordonnée dans une liste "définitive"

def check() :
    #on place une les coordonnées de la première pièces et ensuite la fonction check comparrera à partie de cela
    liste_definitive.append(0)
    liste_definitive.append(0)
    liste_definitive.append(liste_rangée[0])
    liste_definitive.append(liste_rangée[1])
    print("+ 1 pièce")
    #puis pour le nombre de pieces qu'il reste
    for h in range (2,len(liste_rangée),2):
        km=0
        for x in range (largeur) :
            for y in range (longueur) :
                km=km+1
                c=0
                for z in range(4,len(liste_definitive),4):
                    if chev(x,x+liste_rangée[h],liste_definitive[z],liste_definitive[z+2]) and chev(y,y+liste_rangée[h+1],liste_definitive[z+1],liste_definitive[z+3]):
                        c=c+1
                    if not dans(liste_definitive[0],x+liste_rangée[h],liste_definitive[2]) or not dans(liste_definitive[1],y+liste_rangée[h+1],liste_definitive[3]):
                        c=c+1
                    else:
                        c=c
                #si c est égal à 0 alors il peut être placé à ces coordonnés (x,y)
                if not c:
                    liste_definitive.append(x)
                    liste_definitive.append(y)
                    liste_definitive.append(x+liste_rangée[h])
                    liste_definitive.append(y+liste_rangée[h+1])
                    print("+ 1 pièce")
                    km=1
                #si c est différent de 0 alors il ne peut être placé à ces coordonnés (x,y)
                if c:
                    True
        if not km:
            print("la pièce numéro {} n'a pas pu être placée".format(int(h/2)))
    print(liste_definitive)
    
def chev(a,b,c,d):
    if a<b<=c<d or b<a<=c<d or a<b<=d<c or b<a<=d<c:
        return False
    elif c<d<=a<b or d<c<=a<b or c<d<=b<a or d<c<=b<a:
        return False
    else:
        return True

def dans(a,b,c):
    if a<=b<c or c<=b<a:
        return True
    else:
        return False

def mise_aux_dimensions():
    for i in range (0,len(liste_definitive),1):
        liste_definitive[i] = liste_definitive[i]*echelle
    print(liste_definitive)

def jonction():
    c=0
    p=0
    for i in range (6,len(liste_definitive),4):
        if liste_definitive[i]>c :
            c=liste_definitive[i]
            a=i
        if liste_definitive[i+1]>p:
            p=liste_definitive[i+1]
            b=i+1
    liste_definitive[a]=liste_definitive[2]
    liste_definitive[b]=liste_definitive[3]
    print(liste_definitive)

def jonction_():
    n = (((largeur*echelle)/4)*3)
    m = (((longueur*echelle)/4)*3)
    for i in range (6,len(liste_definitive),4):
        if liste_definitive[i] > n :
            liste_definitive[i]=liste_definitive[2]
        if liste_definitive[i+1] > m :
            liste_definitive[i+1]=liste_definitive[3]

def couloir():
    if (len(liste_definitive)/4)-1 > 4 :
        x1 = liste_definitive[4]
        y1 = liste_definitive[5]-(1*echelle)
        x2 = liste_definitive[6]
        y2 = liste_definitive[7]-(1*echelle)
    liste_definitive.append(x1)
    liste_definitive.append(y1)
    liste_definitive.append(x2)
    liste_definitive.append(y2)

def placement():
    x=0
    for i in range(0,len(liste_definitive),4):
        canvas.create_rectangle(liste_definitive[i],liste_definitive[i+1],liste_definitive[i+2],liste_definitive[i+3],fill=color[x])
        x=x+1
    
#Valeurs de base
longueur=10
largeur=20
echelle=40
nb_pieces=8
#Création fenetre et canvas
fenetre=Tk()
canvas=Canvas(fenetre, width=900, height=450, background='#f08080')
canvas.grid(column=0, row=1, ipadx=20, ipady=20)

liste_bazar=[]
liste_rangée=[]
liste_definitive=[]
color=["#FEEAA5","#F5FEA5","#C3FEA5","#A5FEAB","#A5FEDB","#A5FEFE","#A5D2FE","#A8A5FE","#D8A5FE","#FEA5FB"]

liste_definitive.extend([0,0,largeur, longueur])

pieces()
tri()
check()
mise_aux_dimensions()
jonction_()
couloir()
placement()



