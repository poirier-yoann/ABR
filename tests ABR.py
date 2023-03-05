from BinTree import*


test = [42,12,26,35,29,22,56,44,9]


def creerABR(valeurs:list)->BinTree:
    if len(valeurs) == 0:
        return BinTree()
    else :
        sorted(valeurs)
        ABR = BinTree()
        return ABR.setRacine(valeurs[len(valeurs)//2])
        "ABR.setGauche(creerABR(valeurs[:len(valeurs)//2])),ABR.Droit(creerABR(valeurs[len(valeurs)//2:]))"


print(creerABR(test))
print(test[len(test)//2])