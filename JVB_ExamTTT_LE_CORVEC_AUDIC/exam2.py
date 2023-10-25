#exercice 1
#teste si dessous
#def grille(tab):
    #tab1 = [0]*3
    #tab2 = [0]*3
    #tab3 = [0]*3
    #tab = [tab1,tab2,tab3]
    #return(tab)
#ou
#le code si dessous permet d avoir une vrai grille mais je ne sais comme y acceder
tab = [0]*3
for i in range (3):
    print(tab)

#exercice 2

def ajouter(ligne,colone,tab):
    for l in range(len(ligne)):
        for c in range(len(colone)):
            tab.insert(l,c)
    return(tab)

def ranger(tab):
    choix_ligne = int(input("entrez la ligne \n"))
    choix_colone = int(input("entrez la colone \n"))
    choix_symbole = str(input("entrez le symbole entre X et O \n"))
    if choix_ligne == 1 and choix_colone == 1:
        ajouter(choix_symbole,0)
    if choix_ligne == 1 and choix_colone == 2:
        ajouter(choix_symbole,1)
    if choix_ligne == 1 and choix_colone == 3:
        ajouter(choix_symbole,2)
    if choix_ligne == 2 and choix_colone == 1:
        ajouter(choix_symbole,3)
    if choix_ligne == 2 and choix_colone == 2:
        ajouter(choix_symbole,4)
    if choix_ligne == 2 and choix_colone == 3:
        ajouter(choix_symbole,5)
    if choix_ligne == 3 and choix_colone == 1:
        ajouter(choix_symbole,6)
    if choix_ligne == 3 and choix_colone == 2:
        ajouter(choix_symbole,7)
    if choix_ligne == 3 and choix_colone == 1:
        ajouter(choix_symbole,8)



#exercice 4
#Un peu comme un tri a bulle, Quand le joueur entrera une valeur elle sera directement envoyer en bas du tableau 
#et quand il remttretra une valeur au meme enplacement au lieur d etre changer la valeur ira à la ligne d'au dessus.
#Quand 4 valeurs cote a cote sont les meme sinon quand la grille est pleine <--- cela veut donc dire qu il y a une egalité.


