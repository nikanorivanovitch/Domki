import random
from tkinter import *

#Création d'un première liste contenant un nombre de pièces aléatoire
#Chaque pièces est défini par deux points de coordonnées (x,y)
#Les coordonnées sont misent en "bazar", elles ne sont pas oraganisées

def pieces():
    aire=0
    while aire<largeur*longueur*(7/10):
        x=random.randint(2,int(largeur/2))
        y=random.randint(2,int(longueur/2))
        liste_bazar.extend([x,y])
        aire=aire+x*y
    print("$: Pièces définies")
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
    print("$: Tri effectué")
    print(liste_rangée)

#Maintenant que nous avons toutes les coordonnées rangée,
#On vérifie que celle-ci ne se superposent pas ou ne sont pas l'une dans l'autre
#On crée donc la fonction "check" qui rangerais les coordonnée dans une liste "définitive"

def placement() :
    #on place une les coordonnées de la première pièces et ensuite la fonction check comparrera à partie de cela
    liste_definitive.append(0)
    liste_definitive.append(0)
    liste_definitive.append(liste_rangée[0])
    liste_definitive.append(liste_rangée[1])
    print("$: pièce n°1 placée")
    print(liste_definitive)
    #puis pour le nombre de pieces qu'il reste
    for h in range (2,len(liste_rangée),2):
        #Pour ne pas tasser toutes les grosses pièces en haut à gauche, on alterne le départ et le sens de déplacement du curseur
        print(h)
        if h%4==0:
            check_pair(h)
        elif h%4!=0:
            check_impair(h)

def check_impair(h):
    #ici on part du coin gauche supérieur
    for x in range (largeur) :
            for y in range (longueur) :
                c=0
                for z in range(4,len(liste_definitive),4):
                    if chev(x,x+liste_rangée[h],liste_definitive[z],liste_definitive[z+2]) and chev(y,y+liste_rangée[h+1],liste_definitive[z+1],liste_definitive[z+3]):
                        c=c+1
                    if not dans(liste_definitive[0],x+liste_rangée[h],liste_definitive[2]+1) or not dans(liste_definitive[1],y+liste_rangée[h+1],liste_definitive[3]+1):
                        c=c+1
                    else:
                        c=c
                #si c est égal à 0 alors il peut être placé à ces coordonnés (x,y)
                if not c:
                    liste_definitive.append(x)
                    liste_definitive.append(y)
                    liste_definitive.append(x+liste_rangée[h])
                    liste_definitive.append(y+liste_rangée[h+1])
                    liste_rangée[h]=0
                    liste_rangée[h+1]=0
                    print("$: pièce n°{} placée".format(int(h/2)+1))
                    return True
                #si c est différent de 0 alors il ne peut être placé à ces coordonnés (x,y)
                if c:
                    True
    print("ERR$: Impossible de placer la pièce numéro {}".format(int(h/2)+1))

def check_pair(h):
    #ici on part du coin droit inférieur
    for x in range (largeur+1,0,-1) :
            for y in range (longueur+2,0,-1) :
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
                    liste_rangée[h]=0
                    liste_rangée[h+1]=0
                    print("$: pièce n°{} placée".format(int(h/2)+1))
                    return True
                #si c est différent de 0 alors il ne peut être placé à ces coordonnés (x,y)
                if c:
                    True
    print("ERR$: Impossible de placer la pièce numéro {}".format(int(h/2)+1))

    
def chev(a,b,c,d):
    if a<b<=c<d or b<a<=c<d or a<b<=d<c or b<a<=d<c:
        return False
    elif c<d<=a<b or d<c<=a<b or c<d<=b<a or d<c<=b<a:
        return False
    else:
        return True

def dans(a,b,c):
    if a<=b<=c or c<=b<=a:
        return True
    else:
        return False
#$# Fonction qui transforme les distances en mètres en distances sur l'écran en pixel #$#
def mise_aux_dimensions():
    for i in range (0,len(liste_definitive),1):
        liste_definitive[i] = liste_definitive[i]*echelle
    print(liste_definitive)

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

def couleur():
    comp_color=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for x in range(50):
        k="#"
        for y in range(6):
            a=random.randint(0,15)
            k=k+comp_color[a]
        color.append(k)

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
        
#$# Fonction finale qui crée les pièces #$#
def dessin():
    x=0
    for i in range(0,len(liste_definitive),4):
        canvas.create_rectangle(liste_definitive[i],liste_definitive[i+1],liste_definitive[i+2],liste_definitive[i+3],fill=color[x])
        x=x+1
    
#Valeurs de base
longueur=20
largeur=20
echelle=30
nb_pieces=8
#Création fenetre et canvas
fenetre=Tk()
canvas=Canvas(fenetre, width=700, height=700, background='#f08080')
canvas.grid(column=0, row=1, ipadx=20, ipady=20)

liste_bazar=[]
liste_rangée=[]
liste_definitive=[]
color=[]

liste_definitive.extend([0,0,largeur, longueur])

couleur()
pieces()
tri()
placement()
mise_aux_dimensions()
couloir()
dessin()


