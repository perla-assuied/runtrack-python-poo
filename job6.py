#"J'ai crée une classe Animal avec un attribut age initialisé à 0 et prenom initialisé à "LUNA" dans son constructeur.J'ai ajouté une méthode vieillir qui incrémente l'age de l'animal de 1.J'ai ajouté une méthode nommer qui prend en paramètre le nom de l'animal."
class Animal:
    def __init__(self):
        self.age = 10
        self.prenom = "LUNA"

    # Méthode pour faire vieillir l'animal
    def vieillir(self):
        self.age += 1

    # Méthode pour nommer l'animal
    def nommer(self, nom):
        self.prenom = nom

# Instanciation d'un objet Animal
animal = Animal()

# Nommer l'animal
animal.nommer("LUNA")

# J'affiche le nom de l'animal
print("Le nom de l'animal est:", animal.prenom)

# J'affiche l'âge de l'animal
print("L'Âge de l'animal:", animal.age)