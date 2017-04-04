from tkinter import *
import time
import random           

def check_intervalle(a,b,c):
    if a<=b<=c or c<=b<=a:
        return True
    else:
        return False

def check_quartier(a,b):
    if a>=b/2:
        return True
    else:
        return False 

def check_bordure(a,b):
    if abs(a-b)>1.2*k_pixel:
        b=a
        return True
    else:
        return False

def creer_piece(a):
    n=0
    while n==0:
        x0=random.randint(LA/4,3*LA/4)+10
        y0=random.randint(LO/4,3*LO/4)+10
        if check_quartier(x0,LA) and check_quartier(y0,LO):
            x1,y1=10+LA,10+LO
        if check_quartier(x0,LA) and not check_quartier(y0,LO):
            x1,y1=10+LA,10
        if not check_quartier(x0,LA) and not check_quartier(y0,LO):
            x1,y1=10,10
        if not check_quartier(x0,LA) and check_quartier(y0,LO):
            x1,y1=10,10+LO
        for c in range(0,len(a),4):
            if not check_bordure(a[c],x0):
                x0=a[c]
            if not check_bordure(a[c+1],y0):
                y0=a[c+1]
            if not check_intervalle(a[c],x0,a[c+2]) and not check_intervalle(a[c+1],y0,a[c+3]):
                n=1
            else:
                n=0
    a.append(x0)
    a.append(y0)
    a.append(x1)
    a.append(y1)

def dessiner(a,b,c,d):
    canvas.create_rectangle(a,b,c,d)
    
    
        
                
fenetre=Tk()
canvas = Canvas(fenetre, width=1000, height=900, background='yellow')
canvas.pack()

#on pose ; un mètre est rerésenté par 40 pixels.
k_pixel=40
#Les dimensions de la maison
largeur=8
longueur=12
LA=largeur*k_pixel
LO=longueur*k_pixel
#On donne le nombre de pièces ; salon, cuisine, chambre, salle de bain,
a=[1,1,2,1]
canvas.create_rectangle(10,10,10+LA,10+LO)
for x in range(20):
    creer_piece(a)
x=0
for c in range(0,len(a),4):
    dessiner(a[c],a[c+1],a[c+2],a[c+3])
    




