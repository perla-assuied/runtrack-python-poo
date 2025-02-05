#"J'ai mofifié la classe Opération et j'ai ajouter la méthode addition. Elle additione le nombre1 et le nombre2."
class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est:", resultat)

# Je crée une instance de la classe opération
operation = Operation(12,3)

# J'appellle la méthode addition
operation.addition()