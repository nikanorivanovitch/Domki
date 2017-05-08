import random
from tkinter import *

####################################
# Fonction de découpage des pièces #
####################################

#Création d'un première liste contenant un nombre de pièces aléatoire
#Chaque pièce est définie par deux entiers (x,y) qui sont les coordonnées
#Les coordonnées sont misent en "bazar", elles ne sont pas oraganisées

def pieces():
    i = 0 # i sera ici le nombre de pièces créées
    aire_totale=longueur*largeur # aire_totale sera ici le nombre de mètres carrés restant
    while i != nb_pieces-1:
        x = random.randint(int(largeur/5),int(largeur/2)) # ici on définit la largeur de la pièce (largeur sur le plan)
        y = random.randint(int(longueur/5),int(longueur/2)) # et ici on définit la hauteur de la pièce (hauteur sur le plan)
        aire = x*y
        # Et ensuite on lui fait passer des "tests" pour savoir si la pièce est bien découpée
        if aire_totale - aire <= largeur*longueur/25 : # S'il reste moins de 25% de l'aire totale de libre en comptant l'ajout de cette pièce
            print("$: Nous avons créé seulement {} pièces car il n'y a pas assez de place".format(i)) # Alors on affiche un message d'erreur
            break # Et on arrête la boucle
        if 2 >= x-y >=-2 and aire_totale - aire >= 0 : # Si la différence entre la largeur et la hauteur de la pièce n'excède pas 2
            aire_totale = aire_totale - aire # Alors on met à jour le nombre de mètre carrés restant
            i = i+1 # On ajoute 1 au nombre de pièces créées
            liste_bazar.append(x) # et on ajoute les dimensions de la pièce à la liste
            liste_bazar.append(y)
    print("$: Pièces définies :{}".format(i)) # On affiche le nombre de pièces créées
    print(liste_bazar) # On affiche les dimensions des pièces 


################################################
# Fonction de rangement de valeurs d'une liste #
################################################

def tri():
    c=0 # c sera le curseur qui marquera la valeur maximale 
    k=0 # k sera le curseur qui marquera la position de la valeur maximale dans la liste
    for y in range (0,len(liste_bazar),2): # pour chaque couple de la liste_bazar
        c=0 # on met remet c à 0
        for x in range (0,len(liste_bazar),2): # pour chaque couple de la liste_bazar
            if liste_bazar[x]*liste_bazar[x+1]>c: # si l'aire de la pièce (produit des dimensions liste_bazar[x],liste_bazar[x+1] de la pièce de rang x) est supérieure à c
                c=liste_bazar[x]*liste_bazar[x+1] # alors c prend la valeur la plus haute qu'il a pu rencontrer
                k=x # et on note le rang de la valeur maximale 
            else: # si c est supérieur à l'aire de la pièce de rang x, x+1
                c=c # alors c garde sa valeur
        liste_rangée.append(liste_bazar[k]) # à la fin de la deuxième boucle, on ajoute la pièce d'aire maximale à la liste rangée
        liste_rangée.append(liste_bazar[k+1])
        liste_bazar[k],liste_bazar[k+1]=0,0 # et on enlève la pièce de la liste_bazar
    print("$: Tri effectué") # à la fin de la première boucle, on affiche la liste triée
    print(liste_rangée)
    
    
####################################################
# Fonction qui lance le placement des pièces crées #
####################################################

def placement() :
    liste_definitive.append(0) # On place la première pièce de façon manuelle (en haut à gauche de la fenêtre)
    liste_definitive.append(0) 
    liste_definitive.append(liste_rangée[0])
    liste_definitive.append(liste_rangée[1])
    print("$: pièce n°1 placée") # On rend compte du placement de la première pièce
    for h in range (2,len(liste_rangée),2): # Puis pour le nombre de pieces qu'il reste
        check_impair(h) # Et on lance la fonction qui va placer la pièce désignée par la boucle
        
        
#######################################
# Fonction qui place les pièces crées #
#######################################

def check_impair(h):
    # ici on part du coin gauche supérieur
    for x in range (largeur) : # Les deux boucles servent de moteur pour quadriller à l'échelle d'un mètre toute l'habitation, elles forment un curseur qui se déplace
        for y in range (longueur) : # il faut s'illustrer le coin gauche supérieur de la pièce étant à la position du curseur
            c=0 # ici c sera le compteur de superpositions ou d'erreurs fatales
            for z in range(4,len(liste_definitive),4): # cette dernière boucle parcourt toute les pièces déjà placée dans liste_definitive
                if chev(x,x+liste_rangée[h],liste_definitive[z],liste_definitive[z+2]) and chev(y,y+liste_rangée[h+1],liste_definitive[z+1],liste_definitive[z+3]):
                # S'il y a chevauchement entre la pièce à placer et une pièce déjà existante
                    c=c+1 # Alors on ajoute 1 à c
                if not dans(liste_definitive[0],x+liste_rangée[h],liste_definitive[2]) or not dans(liste_definitive[1],y+liste_rangée[h+1],liste_definitive[3]):
                # Si la pièce à placer sort du cadre de l'habitation
                    c=c+1 # Alors on ajoute 1 à c
                else:# S'il n'y a aucune de ces deux conditions, c n'évolue pas
                    c=c
            #si c est égal à 0 alors il peut être placé à ces coordonnés (x,y) car il n'y a aucune erreur vis à vis des pièces déjà placées
            if not c:
                liste_definitive.append(x) # On ajoute la pièce aux positions ne posant aucune erreur
                liste_definitive.append(y)
                liste_definitive.append(x+liste_rangée[h])
                liste_definitive.append(y+liste_rangée[h+1])
                liste_rangée[h]=0 # On efface les dimensions de la pièce à placer car elle vient d'être placée
                liste_rangée[h+1]=0
                print("$: pièce n°{} placée".format(int(h/2)+1))
                return True # La fonction s'arrête et renvoie une valeur positive
            #si c est différent de 0 alors il ne peut être placé à ces coordonnés (x,y) car il y a au moins une erreur vis à vis des pièces déjà placées
            if c:
                True # Donc on ne fait rien
    print("ERR$: Impossible de placer la pièce numéro {}".format(int(h/2)+1)) # si la boucle est finie et que la pièce n'a pas été placée, alors on affiche un message d'erreur
    return False # et on termine la fonction par une valeur négative


#########################
# Fonctions auxiliaires #
#########################

def chev(a,b,c,d): # Cette fonction définit si [a;b]∩[c,d]=∅ (0), si l'intervalle [a;b] et [c;d] ont des valeurs communes
    # On s'en sert pour définir si deux pièces se supersposent
    if a<b<=c<d or b<a<=c<d or a<b<=d<c or b<a<=d<c:
        return False
    elif c<d<=a<b or d<c<=a<b or c<d<=b<a or d<c<=b<a:
        return False
    else:
        return True

def dans(a,b,c): # Cette fonction définit si b appartient à [a;c]
    if a<=b<=c or c<=b<=a:
        return True
    else:
        return False

    
#######################
# Mise aux dimensions #
#######################

def mise_aux_dimensions():
    for i in range (0,len(liste_definitive),1):
        liste_definitive[i] = liste_definitive[i]*echelle
    print(liste_definitive)

    
###############################################
# Fonction qui rajoute des couloirs si besoin #
###############################################

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
        
        
###################################    
# Fonction qui dessine les pièces #
###################################

def dessin():
    x=0
    for i in range(0,len(liste_definitive),4):
        canvas.create_rectangle(10+liste_definitive[i],10+liste_definitive[i+1],10+liste_definitive[i+2],10+liste_definitive[i+3],fill=color[x])
        x=x+1 # On change l'indice de la couleur
        # On ajoute 10 à chaques dimensions pour qu'on puisse apercevoir une marge autour de la maison, le fill=color[x] permet de colorier la pièce
        # à l'aide d'une couleur déjà définie par la fonction couleur() et stockée dans la liste color


######################################
# Fonction qui fabrique des couleurs #
######################################

def couleur():
    comp_color=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    for x in range(50):
        k="#"
        for y in range(6):
            a=random.randint(0,15)
            k=k+comp_color[a]
        color.append(k)


#########################
# Fonction de "lissage" #
#########################

def jonction():
    for i in range(4,len(liste_definitive),4):
        c=0 # c est encore ici un compteur d'erreur
        for x in range(4,len(liste_definitive),4): # Les deux boucles permettent de traiter chaque pièce placée avec une autre pièce placée
            if x!=i: 
                if chev(liste_definitive[i],liste_definitive[2],liste_definitive[x],liste_definitive[x+2]) and chev(liste_definitive[i+1],liste_definitive[3],liste_definitive[x+1],liste_definitive[x+3]):
                    c=c+1
                if abs(liste_definitive[i+2]-liste_definitive[2])<=2: # S'il existe un espace entre une pièce et le mur extérieur, dont on ne peut rien faire
                    liste_definitive[i+2]=liste_definitive[2]         # alors on agrandit la pièce pour qu'elle touche le mur extérieur
                if abs(liste_definitive[i+3]-liste_definitive[3])<=2:
                    liste_definitive[i+3]=liste_definitive[3]
            if x==i: # Si les deux pièces sont en fait la même, un traitement est inutile
                True
        if not c:
            liste_definitive[i+2]=liste_definitive[2]
            liste_definitive[i+3]=liste_definitive[3]


################################
#------------------------------#
#--------Premère partie--------#
#------------------------------#
################################

#Entrer des valeurs: 
fenetre = Tk()
fenetre.title('Architecktor 2000: maison sur mesure')

#Phrase de présentation
en_tete = Label(fenetre)
en_tete.grid(column= 0, row= 0, columnspan=2, sticky='s', ipady=20)
#Entrer la taille du terrain
texte_terrain = Label(fenetre, text="Veuillez nous donner les dimensions de votre maison (en mètres):", foreground='#f08080' ,font=('Trebuchet','13','bold'))
texte_terrain.grid(column= 0, row= 1, columnspan=2)
#Première zone de saisie: Longueur
longueur_ = IntVar()
longueur = Label(fenetre, text='Longueur de votre maison :',foreground='#f08080' ,font='Trebuchet')
longueur.grid(column= 0, row= 2, sticky='e')
choix_longueur = Spinbox(fenetre, textvariable=longueur_, from_=8, to=35)
choix_longueur.grid(column=1, row=2, sticky='w')
#Première zone de saisie: Largeur
largeur_ = IntVar()
largeur = Label(fenetre, text='Largeur de votre maison :',foreground='#f08080' ,font='Trebuchet')
largeur.grid(column= 0, row= 3, sticky='e')
choix_largeur = Spinbox(fenetre, textvariable=largeur_, from_=8, to=35)
choix_largeur.grid(column=1, row=3, sticky='w')


#Entrer le nombre de pièces
nb_pieces_ = IntVar()
texte_terrain = Label(fenetre, text="Veuillez nous donner le nombre de pièces :", foreground='#f08080' ,font=('Trebuchet','13','bold'))
texte_terrain.grid(column= 0, row= 4, sticky='se')
choix_nb_pieces = Spinbox(fenetre, textvariable=nb_pieces_, from_=3, to=20)
choix_nb_pieces.grid(column=1, row=4, sticky='sw') 

#Bouton
bouton = Button(fenetre, text=" Créer un plan ", foreground='#f08080' ,font='Trebuchet',command=fenetre.destroy)
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

################################
#------------------------------#
#--------Deuxieme partie-------#
#------------------------------#
################################

print(longueur)
print(largeur)
print(nb_pieces)

#Valeurs de base
echelle=30
#Création fenetre et canvas
fenetre=Tk()
H,W=fenetre.winfo_screenheight(),fenetre.winfo_screenwidth()
canvas=Canvas(fenetre, width=W-150, height=H-170, background='#f08080')
canvas.grid(column=0, row=0, ipadx=20, ipady=20)
fenetre.columnconfigure(0, pad= 100)
fenetre.rowconfigure(0, pad=100)

if largeur>longueur:
    echelle = int((H-200)/largeur)
if largeur<longueur:
    echelle = int((H-200)/longueur)
if largeur==longueur:
    echelle = int((H-200)/largeur)
    
canvas.create_line(5,5,5,5+echelle)# ici met l'échelle du repère
canvas.create_line(5,5,5+echelle,5)
liste_bazar=[]
liste_rangée=[]
liste_definitive=[]
color=[]

liste_definitive.extend([0,0,largeur, longueur])

couleur()
pieces()
tri()
placement()
jonction()
mise_aux_dimensions()
dessin()
