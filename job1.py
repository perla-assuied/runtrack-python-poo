#"Je crée une classe Opération avec un constructeur, j'ai ajouté les attributs nombre1 et nombre2, puis j'ai imprimé l'objet en console"
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation()

print(operation)