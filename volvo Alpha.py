from tkinter import *
import time
import random           

def rectangle(a,b,c,d):
    canvas.create_rectangle(a,b,c,d)

def ligne(a,b,c,d):
    canvas.create_line(a,b,c,d)

def piece(a,b,c):
    x0=a-1
    y0=b-1
    canvas.create_rectangle(x0*k_pixel,y0*k_pixel,a*k_pixel,b*k_pixel,fill=c)
                  
fenetre=Tk()
canvas = Canvas(fenetre, width=1000, height=900, background='yellow')
#on pose ; un mètre est rerésenté par 40 pixels.
k_pixel=40
#Les dimensions de la maison
largeur=8
longueur=12
LA=largeur*k_pixel
LO=longueur*k_pixel
canvas.pack()
aire=(largeur*longueur)
a_salon=int(aire/3)
a_chambre=int(aire/3)
a_cuisine=aire-(a_salon+a_chambre)
a=[a_salon,a_chambre,a_cuisine]
c=["red","blue","pink"]
d=0
x=0
y=0
for y in range(1,longueur+1):
    for x in range(1,largeur+1):
        piece(x,y,c[d])
        a[d]=a[d]-1
        if a[d]<0:
            d=d+1
        else:
            d=d

print("fini")      
            
    
    
        
        

