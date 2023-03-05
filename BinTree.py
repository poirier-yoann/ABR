

## Classe
        
class BinTree:
    """
    Classe BinTree
    - Attributs :
        * root : La racine root de type N (ou None)
        * left : Le sous-arbre gauche de type BinTree (ou None)
        * right : Le sous-arbre droit de type BinTree (ou None)
      Un arbre vide est représenté par un objet dont tous les attributs ont la valeur None
      
    - Condition : Un arbre est vide si et seulement si la racine est non définie
    
    - Méthodes :
        * Constructeur : BinTree(root,left,right)
        * estVide()
        * droit()
        * gauche()
        * racine()
        * estFeuille()
        * setGauche()
        * setDroit()
        * setRacine()
        * taille()
        * hauteur()
        * __str__()
    

    
    """
    ## Constructeur
    
    def __init__(self,root=None,left=None,right=None):
        """
        Constructeur de la classe BinTree (avec arguments optionnels, avec valeur None par défaut)
        """
        # Pré-conditions
        assert (isinstance(left,BinTree) or left==None), "L'arbre gauche doit être un BinTree ou None"
        assert (isinstance(right,BinTree) or right==None), "L'arbre droit doit être un BinTree ou None"
        
        self.__root=root
        self.__left=left
        self.__right=right
        
        #  Axiome
        assert (self.estVide()==(self.__root==None)), "Un arbre non vide a une racine"


    ## Méthodes
    
    def droit(self):
        """
        Renvoie le sous-arbre droit (un arbre vide si l'arbre droit vaut None)
        """
        if self.__right==None:
            return BinTree()
        else :
            return self.__right
    
    def gauche(self):
        """
        Renvoie le sous-arbre gauche (un arbre vide si l'arbre gauche vaut None).
        """
        if self.__left==None:
            return BinTree()
        else :
            return self.__left
    
    def racine(self):
        """
        Renvoie la valeur de la racine A de l'arbre, None si l'arbre est vide.
        """
        return self.__root
    
    def estVide(self):
        """
        Renvoie True si l'arbre est vide.
        """
        return (self.__root==None) and (self.__left==None) and (self.__right==None)
    
    
    
    def estFeuille(self)->bool:
        """
        Renvoie True si l'arbre est une feuille.
        """
        # Modification code
        # return self.__left==None and self.__right==None and not(self.__root==None)
        return self.gauche().estVide() and self.droit().estVide()
        
    def setDroit(self,B):
        """
        L'arbre droit devient B.
        """
        assert not(self.estVide()), "On ne peut modifier modifier les sous_arbres de l'arbe vide"
        assert (isinstance(B,BinTree) or B==None), "L'argument doit être une instance de BinTree ou None"
        self.__right=B
    
    def setGauche(self,B):
        """
        L'arbre gauche devient B.
        """
        assert not(self.estVide()), "On ne peut modifier les sous_arbres d'un arbe vide"
        assert (isinstance(B,BinTree) or B==None), "L'argument doit être une instance de BinTree ou None"
        self.__left=B
        
    def setRacine(self,r):
        """
        La valeur de la racine devient r.
        """
        self.__root=r
        
    ## Mesures  
    
    def taille(self)->int:
        """
        Renvoie la taille de l'arbre A
        """
        if self.estVide():
            return 0
        else :
            return 1+self.gauche().taille()+self.droit().taille()
            
    def hauteur(self):
        """
        Renvoie la hauteur de l'arbre A
        """
        if self.estVide():
            return -1
        else :
            return 1+max(self.gauche().hauteur(),self.droit().droit().hauteur())

 
    
    ## Impression
    def __str__(self,n=0,car=""):
        """
        Fournit une vue lisible de l'arbre.
        """
        if not(self.estVide()):
            self.droit().__str__(n+4,'/')
            print(n*" "+car,end=" ")
            print(self.racine())
            self.gauche().__str__(n+4,'\\')
        elif n==0:
            #Imprime "arbre_vide" si l'arbre est vide (lors de l'appel initial)
            print("Arbre_vide")
        
        #La fonction doit renvoyer une chaîne, mais l'impression est déjà gerée plus haut 
        return ""


"""
## Tests

# Création de l'arbre python
python=BinTree("T",BinTree("Y",BinTree("P")),BinTree("O",BinTree("H"),BinTree("N")))

# Création d'un arbre vide
arbre_vide=BinTree()

# Création d'une feuille (avec valeur entière)
feuille=BinTree(5)

#Création du jeu de test
jeu=[arbre_vide,feuille,python]

#Test méthodes
def TestBinTree(jeu:list):
    for A in jeu :
        print("Test : \n",A)
        print("estVide() : ",A.estVide())
        print("droit() : \n",A.droit())
        print("gauche() : \n",A.gauche())
        print("racine() : ",A.racine())
        print("estFeuille() : ",A.estFeuille())
        print("taille() : ",A.taille())
        print("hauteur() :",A.hauteur())
        A.setRacine("TestR")
        print("modification racine :\n ",A)
        A.setGauche(BinTree("TestG"))
        print("modification arbre gauche :\n ",A)
        A.setDroit(BinTree("TestD"))
        print("modification arbre droit :\n ",A)


TestBinTree(jeu)
"""





             
        