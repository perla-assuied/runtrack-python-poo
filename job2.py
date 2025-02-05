#" A l'aide de la classe Opération, j'ai imprimé en consoleles valaurs des attributs nombre1 et nombre2"
class Operation:
    def __init__(self, nombre1=2, nombre2=12):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

operation = Operation()

print("nombre1:", operation.nombre1)
print("nombre2:", operation.nombre2)