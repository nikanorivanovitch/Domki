import random
from tkinter import *

#Création d'un première liste contenant un nombre de pièces aléatoire
#Chaque pièces est défini par deux points de coordonnées (x,y)
#Les coordonnées sont misent en "bazar", elles ne sont pas oraganisées

def pieces_():
    i = 0
    aire_totale=longueur*largeur
    while i != nb_pieces:
        x = random.randint(int(largeur/5),int(largeur/2))
        y = random.randint(int(longueur/5),int(longueur/2))
        aire = x*y
        if aire_totale - aire <= largeur*longueur/25 :
            print("$: Nous avons placé seulement placé {} pièces car il n'y a pas assez de place".format(i))
            break
        if 2 >= x-y >=-2 and aire_totale - aire >= largeur*longueur/25 :
            aire_totale = aire_totale - aire
            i = i+1
            liste_bazar.append(x)
            liste_bazar.append(y)
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
        check_impair(h)

def check_impair(h):
    #ici on part du coin gauche supérieur
    for x in range (largeur) :
        for y in range (longueur) :
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

def chev_(a,b,c,d):
    if a<b<=c<d or b<a<=c<d or a<b<=d<c or b<a<=d<c:
        return False
    elif c<d<=a<b or d<c<=a<b or c<d<=b<a or d<c<=b<a:
        return False
    if c==a and b>d:
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
       
#$# Fonction finale qui crée les pièces #$#
def dessin():
    x=0
    for i in range(0,len(liste_definitive),4):
        canvas.create_rectangle(liste_definitive[i],liste_definitive[i+1],liste_definitive[i+2],liste_definitive[i+3],fill=color[x])
        x=x+1

def couleur():
    comp_color=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for x in range(50):
        k="#"
        for y in range(6):
            a=random.randint(0,15)
            k=k+comp_color[a]
        color.append(k)

def jonction():
    for i in range(4,len(liste_definitive),4):
        c=0
        for x in range(4,len(liste_definitive),4):
            if x!=i:
                if chev(liste_definitive[i],liste_definitive[2],liste_definitive[x],liste_definitive[x+2]) and chev(liste_definitive[i+1],liste_definitive[3],liste_definitive[x+1],liste_definitive[x+3]):
                    c=c+1
            if x==i:
                True
        if not c:
            liste_definitive[i+2]=liste_definitive[2]
            liste_definitive[i+3]=liste_definitive[3]
        print(c)
                
            
            

def jonction_():
    n = (((largeur*echelle)/4)*3)
    m = (((longueur*echelle)/4)*3)
    for i in range (6,len(liste_definitive),4):
        if liste_definitive[i] > n :
            liste_definitive[i]=liste_definitive[2]
        if liste_definitive[i+1] > m :
            liste_definitive[i+1]=liste_definitive[3]

#------------------------------
#--------Premère partie--------
#------------------------------

#Entrer des valeurs: 
fenetre = Tk()
fenetre.title('Architecktor 2000: maison sur mesure')

#Phrase de présentation
en_tete = Label(fenetre)
en_tete.grid(column= 0, row= 0, columnspan=2, sticky='s', ipady=20)
#Entrer la taille du terrain
texte_terrain = Label(fenetre, text="Veuillez nous donner les dimensions de votre terrain (en mètres):", foreground='#f08080' ,font=('Trebuchet','13','bold'))
texte_terrain.grid(column= 0, row= 1, columnspan=2)
#Première zone de saisie: Longueur
longueur_ = IntVar()
longueur = Label(fenetre, text='Longueur de votre terrain:',foreground='#f08080' ,font='Trebuchet')
longueur.grid(column= 0, row= 2, sticky='e')
choix_longueur = Spinbox(fenetre, textvariable=longueur_, from_=5, to=35)
choix_longueur.grid(column=1, row=2, sticky='w')
#Première zone de saisie: Largeur
largeur_ = IntVar()
largeur = Label(fenetre, text='Largeur de votre terrain:',foreground='#f08080' ,font='Trebuchet')
largeur.grid(column= 0, row= 3, sticky='e')
choix_largeur = Spinbox(fenetre, textvariable=largeur_, from_=5, to=35)
choix_largeur.grid(column=1, row=3, sticky='w')


#Entrer le nombre de pièces
nb_pieces_ = IntVar()
texte_terrain = Label(fenetre, text="Veuillez nous donner le nombre de pièces:", foreground='#f08080' ,font=('Trebuchet','13','bold'))
texte_terrain.grid(column= 0, row= 4, sticky='se')
choix_nb_pieces = Spinbox(fenetre, textvariable=nb_pieces_, from_=1, to=20)
choix_nb_pieces.grid(column=1, row=4, sticky='sw') 

#Bouton
bouton = Button(fenetre, text="Suivant", foreground='#f08080' ,font='Trebuchet',command=fenetre.destroy)
bouton.grid(column=0, row=10, columnspan=2)            

#Les marges
fenetre.columnconfigure(0, pad=400)
fenetre.columnconfigure(1, pad=400)
fenetre.rowconfigure(0, pad=30)
fenetre.rowconfigure(4, pad=20)
fenetre.rowconfigure(10, pad=50)

fenetre.mainloop()

longueur=longueur_.get()
largeur=largeur_.get()
nb_pieces=nb_pieces_.get()

#------------------------------
#--------Deuxieme partie--------
#------------------------------

print(longueur)
print(largeur)
print(nb_pieces)

#Valeurs de base
echelle=30
#Création fenetre et canvas
fenetre=Tk()
canvas=Canvas(fenetre, width=largeur*echelle+100, height=longueur*echelle+100, background='#f08080')
canvas.grid(column=0, row=0, ipadx=20, ipady=20)
fenetre.columnconfigure(0, pad= 100)
fenetre.rowconfigure(0, pad=100)

liste_bazar=[]
liste_rangée=[]
liste_definitive=[]
color=[]

liste_definitive.extend([0,0,largeur, longueur])

couleur()
pieces_()
tri()
placement()
jonction()
mise_aux_dimensions()
dessin()
