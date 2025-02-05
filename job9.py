 # J'ai crée une classe Produit avec les attributs nom, prixHT et TVA. J'ai ajouté la méthode pour calculer le prix TTC, afficher les informations du produit, modifier le nom et le prix du produit. J'ai crée plusieurs produits et j'ai affiché les informations initiales des produits. J'ai modifié le nom et le prix des produits et j'ai affiché les nouvelles informations après modifications. J'ai utilisé la méthode afficher pour afficher les informations des produits.
class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
 
    # Méthode pour calculer le prix TTC
    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    # Méthode pour afficher les informations du produit
    def afficher(self):
        return {
            'Nom': self.nom,
            'Prix HT': self.prixHT,
            'TVA': self.TVA,
            'Prix TTC': self.calculerPrixTTC()
        }

    # Méthode pour modifier le nom du produit
    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    # Méthode pour modifier le prix HT du produit
    def modifierPrix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    # Méthode pour retourner le nom 
    def getNom(self):
        return self.nom

    # Méthode pour retourner le prix HT
    def getPrixHT(self):
        return self.prixHT

    # Méthode pour retourner la TVA
    def getTVA(self):
        return self.TVA

    # Méthode pour retourner le prix TTC
    def getPrixTTC(self):
        return self.calculerPrixTTC()

# J'ai crée plusieurs produits 
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 150, 10)
produit3 = Produit("Produit C", 200, 5)

# J'affiche les informations initiales des produits
print("Informations des produits initiaux:")
for produit in [produit1, produit2, produit3]:
    infos = produit.afficher()
    print(infos)

# Je modofoe le nom et le prix des produits
produit1.modifierNom("Produit A modifié")
produit1.modifierPrix(120)

produit2.modifierNom("Produit B modifié")
produit2.modifierPrix(180)

produit3.modifierNom("Produit C modifié")
produit3.modifierPrix(220)

# J'affiche les nouvelles informations après modifications
print("\nInformations des produits après modification:")
for produit in [produit1, produit2, produit3]:
    infos = produit.afficher()
    print(infos)