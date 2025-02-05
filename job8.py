# J'ai crée une classe Cercle, j'ai ajouté la méthode pour changer le rayon, afficher les informations du cercle, calculer la circonférence, l'aire et le diamètre du cercle. J'ai aussi ajouté deux instances de la classe Cercle avec les rayons 4 et 7. J'ai affiché les informations, la circonférence, l'aire et le diamètre de chaque cercle.
import math
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    # Je modifie le rayon du cercle
    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    # J'affiche les informations du cercle, le rayon, le diamètre, la circonférence et l'aire
    def afficherInfos(self):
        print(f"Rayon: {self.rayon}")
        print(f"Diamètre: {self.diametre()}")
        print(f"Circonférence: {self.circonference()}")
        print(f"Aire: {self.aire()}")
    
    # C'est la méthode pour calculer la circonférence du cercle (2 * pi * rayon)
    def circonference(self):
        return 2 * math.pi * self.rayon

    # C'est la méthode pour calculer l'aire du cercle (pi * rayon^2)
    def aire(self):
        return math.pi * (self.rayon ** 2)

    # C'est la méthode pour retourner le diamètre du cercle (2 * rayon)
    def diametre(self):
        return 2 * self.rayon

# Je crée deux cercles avec les rayons 5 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# J'affiche les infos du premier cercle 
print("Cercle 1:")
cercle1.afficherInfos()
print("\n")

# J'affiche les infos du deuxième cercle
print("Cercle 2:")
cercle2.afficherInfos()
print("\n")