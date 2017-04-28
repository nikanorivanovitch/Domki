import random
from tkinter import *

#fonction faite pour prendre une décision aléatoire réduite à un "oui"/"non"
def hasard():
    a=random.randint(0,1)
    if a==True:
        return True
    elif a==False:
        return False

#fonction qui créer les rectangles donc les coordonnées ont été stockées dans une liste, elle est utilisée à la fin
def dessiner_rec():
    for x in range(0,len(pos_rec),4):
        canvas.create_rectangle(pos_rec[x],pos_rec[x+1],pos_rec[x+2],pos_rec[x+3])

#fonction importante /!\ qui définit aléatoirement les dimensions d'une pièce
def piece(a):
    #ici on comprend que la pièce ne doit pas être plus petite que 2m sur 2m et plus grande qu'un quart de la maison
    x=random.randint(2,int(largeur/2))
    y=random.randint(2,int(hauteur/2))
    liste.append(x)
    liste.append(y)
    return x*y

#fonction importante /!\ qui crée les pièces qu'il va y avoir dans la maison, elle utilise la fonction piece(a)
def decoupage(a):
    n=0
    k=0
    while n==0:
        #tant que n est égal à zéro, on continue la boucle qui lance la fonction pièce(a), ici "a" c'est l'aire totale de toutes les pièces (aire renvoyée
        #par le "return x*y" de la fonction piece(a)
        a=a+piece(a)
        #ici k sert à compter le nombre de pièces qui ont été crées
        k=k+1
        if a>(5/10)*hauteur*largeur:
            #si l'aire de toutes les pièces est supérieure à plus de 60% de l'aire totale de la maison, on arrête donc on casse la boucle en donnant n=1
            n=1
    #on donne les résultats de la fonction
    print("Nous avons {} pièces et {} m²".format(k,a))

#fonction assez simple qui trie les valeurs d'une chaine (valeurs sous forme de couple)
def tri_liste():
    c=0
    k=0
    for y in range(0,len(liste),2):
        c=0
        for x in range(0,len(liste),2):
            if liste[x]*liste[x+1]>c:
                c=liste[x]*liste[x+1]
                k=x
            else:
                c=c
        liste_t_rec.append(liste[k])
        liste_t_rec.append(liste[k+1])
        liste[k],liste[k+1]=0,0

#fonction importante /!\ plus évoluée que son homonyme, elle trie les valeurs en les remettant dans la même liste
def tri_liste_t_rec():
    c=0
    k=0
    l_s=[]
    for y in range(0,len(liste_t_rec),2):
        c=0
        for x in range(0,len(liste_t_rec),2):
            if liste_t_rec[x]*liste_t_rec[x+1]>c:
                c=liste_t_rec[x]*liste_t_rec[x+1]
                k=x
            else:
                c=c
        l_s.append(liste_t_rec[k])
        l_s.append(liste_t_rec[k+1])
        liste_t_rec[k],liste_t_rec[k+1]=0,0
    for x in range(len(l_s)):
       liste_t_rec[x]=l_s[x]+0

#fonction assez foireuse et inutile car elle effectue une fusion de salles si c'est possible (à supprimer si trop lourd)
def assemblage(a,b):
    if a==b:
        return 0
    elif a!=b and liste_t_rec[a]==liste_t_rec[b] and liste_t_rec[a+1]==liste_t_rec[b+1]:
        if hauteur>largeur and 2*liste[b+1]<=hauteur:
            liste_t_rec[a+1]=2*liste[b+1]
            liste_t_rec[b]=0
            liste_t_rec[b+1]=0
            liste_t_lig.append(a)
            print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
        if hauteur<largeur and 2*liste_t_rec[b]<=largeur:
            liste_t_rec[a]=2*liste_t_rec[b]
            liste_t_rec[b]=0
            liste_t_rec[b+1]=0
            liste_t_lig.append(a)
            print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
        if hauteur==largeur:
            if 2*liste_t_rec[b]<=largeur and 2*liste[b+1]<=hauteur:
                if hasard():
                    liste_t_rec[a+1]=2*liste_t_rec[b+1]
                    liste_t_rec[b]=0
                    liste_t_rec[b+1]=0
                    liste_t_lig.append(a)
                    print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
                if not hasard():
                    liste_t_rec[a]=2*liste_t_rec[b]
                    liste_t_rec[b]=0
                    liste_t_rec[b+1]=0
                    liste_t_lig.append(a)
                    print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
            if 2*liste_t_rec[b]<=largeur and 2*liste_t_rec[b+1]>hauteur:
                liste_t_rec[a]=2*liste_t_rec[b]
                liste_t_rec[b]=0
                liste_t_rec[b+1]=0
                liste_t_lig.append(a)
                print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
            if 2*liste_t_rec[b]>largeur and 2*liste_t_rec[b+1]<=hauteur:
                liste_t_rec[a+1]=2*liste_t_rec[b+1]
                liste_t_rec[b]=0
                liste_t_rec[b+1]=0
                liste_t_lig.append(a)
                print("fusion effectuée entre la {}ème pièce et la {}ème pièce".format((a/2)+1,(b/2)+1))
            if 2*liste_t_rec[b]>largeur and 2*liste_t_rec[b+1]>hauteur:
                print("ERREUR: la {}ème pièce et la {}ème pièce ne sont pas compatibles".format(a/2,b/2))
    else:
        return 0

#fonction qui définit si un nombre b appartient à l'intervale [a,c]
def dans(a,b,c):
    if a<=b<c or c<=b<a:
        return True
    else:
        return False

#fonction qui pose la première pièce (c'est plus facile comme ça) elle sert à ajouter un premier contenu à la liste des positions pour la fonctiond dessiner()
def put_first():
    pos_rec.append(0)
    pos_rec.append(0)
    pos_rec.append(liste_t_rec[0])
    pos_rec.append(liste_t_rec[1])

#fonction chevauchement
def chev(a,b,c,d):
    if a<b<=c<d or b<a<=c<d or a<b<=d<c or b<a<=d<c:
        return False
    elif c<d<=a<b or d<c<=a<b or c<d<=b<a or d<c<=b<a:
        return False
    else:
        return True

#fonction importante /!\ qui regarde si deux pièces sont superposée, cette fonction gère le placement des pièces
def check(x,y,a):
    c=0
    for z in range(4,len(pos_rec),4):
        if chev(x,x+liste_t_rec[a],pos_rec[z],pos_rec[z+2]) and chev(y,y+liste_t_rec[a+1],pos_rec[z+1],pos_rec[z+3]):
            c=c+1
        if not dans(pos_rec[0],x+liste_t_rec[a],pos_rec[2]) or not dans(pos_rec[1],y+liste_t_rec[a+1],pos_rec[3]):
            c=c+1
        else:
            c=c
    if not c:
        return True
    if c:
        return False
        
#fonction importante /!\ elle place les pièces (à expliquer oralement parceque trop compliquée)
def put(a):
    x=-1
    y=0
    while y!=11:
        x=x+1
        if x==11:
            y=y+1
            x=0
        if check(x,y,a):
            pos_rec.append(x)
            pos_rec.append(y)
            pos_rec.append(x+liste_t_rec[a])
            pos_rec.append(y+liste_t_rec[a+1])
            print("la pièce {} a été placée aux positions {} {}".format(a/2,x,y))
            return True
        else:
            True
    return False
            
#fontion principale du programme
def main():
    put_first()
    for ka in range(2,len(liste_t_rec),2):
        put(ka)
        print(liste_t_rec[ka])
    
                    
hauteur=15
largeur=15
kp=40
pos_rec=[]
liste=[]
liste_t_rec=[]
liste_t_lig=[]
liste_pol=[]
pos_rec.append(0)
pos_rec.append(0)
pos_rec.append(largeur)
pos_rec.append(hauteur)
pieces=5
a=0
fenetre=Tk()
canvas=Canvas(fenetre, width=800, height=600, background='red')
canvas.pack()
decoupage(a)
print(liste)
tri_liste()
print(liste_t_rec)
main()
for x in range(len(pos_rec)):
    pos_rec[x]=pos_rec[x]*kp
print(pos_rec)
dessiner_rec()




