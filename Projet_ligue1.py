import csv


Listes_joueur = []
with open("Joueurs.csv", mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        Listes_joueur.append(line.split(";"))

for i, tab in enumerate(Listes_joueur):
    Listes_joueur[i][-1] = tab[-1].strip()  
print(Listes_joueur)

 
'''def selection_donees(l:list,i = 0,x=8,):
    nombre_elt = len(l)-1
    if x == nombre_elt :
        return l
    else :
        while i <= nombre_elt :
                l[i].pop(x)
                i = i+1
        else:
            selection_donees(l,i-(nombre_elt-1),x +1)
    


selection_donees(Listes_joueur)



Dans la listes, il y a des listes separees par des virgules qui contiennent chacune les info des differents joueurs
Exemple d'element de la liste:
[306,Jonas Martin,fr FRA,MT,Lille,32-200,1990,7,1,148,1.6,0,0,0,0,0,1,0,0.00,0.00,0.00,0.00,0.00,0.0,0.0,0.0,0.0,0.00,0.01,0.01,0.00,0.01,Matchs,468fdbad']
'''