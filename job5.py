#"Je créé une classe Point avec les attributs x et y qui correspondent aux coordonnées horizontales et verticales du point. J'initialise les deux attributs dans le constructeur."
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # J'affiche les coordonées du point
    def afficherLesPoints(self):
        print(f"Point: ({self.x}, {self.y})")

    # J'affiche la coordonnée x
    def afficherX(self):
        print(f"Coordonnée x: {self.x}")

    # J'affiche la coordonnée y
    def afficherY(self):
        print(f"Coordonnée y: {self.y}")

    # Je change la valeur de x
    def changerX(self, nouvelle_x):
        self.x = nouvelle_x
        print(f"Nouvelle coordonné x: {self.x}")

    # Je change la valeur de y
    def changerY(self, nouvelle_y):
        self.y = nouvelle_y
        print(f"Nouvelle coordonnée y: {self.y}")

# Instanciation des objets Point
point1 = Point(3, 4)
point2 = Point(7, 2)

# Pour le premier point
point1.afficherLesPoints()  # Affiche les coordonnés du point
point1.afficherX()  # Affiche X
point1.afficherY()  # Affiche Y

# Je change les coordonnées
point1.changerX(10)
point1.changerY(20)
point1.afficherLesPoints()  # Affiche les coordonnés du points

# Pour le deuxième point
point2.afficherLesPoints()
point2.afficherX()
point2.afficherY()