class Animal:
    def __init__(self, nome):
        self.nome = nome

    def registrar(self):
        pass

class Cachorro(Animal):
    def registrar(self):
        return f"Cachorro {self.nome} registrado para consulta."

class Gato(Animal):
    def registrar(self):
        return f"Gato {self.nome} registrado para consulta."

# Demonstração do Polimorfismo
pacientes = [Cachorro("Rex"), Gato("Mia")]

for animal in pacientes:
    print(animal.registrar())
