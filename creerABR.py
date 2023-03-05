from BinTree import *

test = [30,41,25,52,29,18,9,46,60,26,28]
"""
def creerBinTree(valeurs)->BinTree :
    if len(valeurs) == 0:
        return BinTree()
    
    elif len(valeurs) == 1 :
        return BinTree(valeurs[0])
    
    else:
        # valeurs.sort()
        milieu = len(valeurs) // 2
        return BinTree(valeurs[milieu], creerBinTree(valeurs[:milieu]), creerBinTree(valeurs[milieu+1:]))

def creerABR(valeurs):
    return creerBinTree(sorted(valeurs))

print(creerABR(test))
"""

def inserecle(valeurs, ABR)->BinTree:
    if ABR.racine() is None:
        ABR.setRacine(valeurs)
    elif valeurs <= ABR.racine():
        ABR.setGauche(inserecle(valeurs, ABR.gauche()))
    elif valeurs > ABR.racine():
        ABR.setDroit(inserecle(valeurs, ABR.droit()))

    return ABR
    
def creerABR(liste_valeurs):
    arbre = BinTree()
    for valeur in liste_valeurs:
        inserecle(valeur, arbre)

    return arbre
    
arbre = creerABR(test)
print(arbre)

"""
tree = ABR()

for v in test:
    tree.insert(v)
"""