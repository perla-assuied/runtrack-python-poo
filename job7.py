# J'ai créee une classe Personnage avec les attributs x et y qui correspondent aux coordonnées horizontales et verticales du personnage. J'initialise les deux attributs dans le constructeur. J'ai aussi crée les méthodes gauche, droite, haut et bas qui permet de faire avancer le personnage, j'ai ajouté la méthode qui retourne les positions sous forme d'un tuple.
class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

     # Je déplace le personnage vers la gauche, ca diminue x
    def gauche(self):
        self.x -= 1

     #Je déplace le personnage vers la droite, ca augmente x 
    def droite(self):
        self.x += 1

     #Je déplace le personnage vers le haut, ca diminue y
    def haut(self):
        self.y -= 1

     #Je déplace le personnage vers le bas, ca augmente y
    def bas(self):
        self.y += 1

    # Méthode pour afficher la position du personnage
    def position(self):
        return (self.x, self.y)

# Création d'un objet Personnage avec des coordonnées initiales (2, 3)
personnage = Personnage(2, 3)

# J'affiche de la position initiale
print("Position initiale:", personnage.position())

# Déplacement du personnage
personnage.gauche()  # Déplacement à gauche
personnage.haut()    # Déplacement vers le haut

# J'Affiche la nouvelle position après les déplacements
print("Nouvelle position après déplacements:", personnage.position())

# Déplacement vers la droite et vers le bas
personnage.droite()
personnage.bas()

# J'affiche la position après ces derniers déplacements
print("Position après autres déplacements:", personnage.position())