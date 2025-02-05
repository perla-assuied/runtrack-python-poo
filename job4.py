# "J'ai crée une classe Personne avec les attributs nom et prénom, j'ai ajouter une méthode SePrésenter qui vas retourner le nom et le prénom."
class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}."

# Instanciation des objets Personne
personne1 = Personne("Doe", "Jonh")
personne2 = Personne("Dupond", "Jean")

# J'appel la méthode SePresenter dans toutes les instances
print(personne1.SePresenter())
print(personne2.SePresenter())