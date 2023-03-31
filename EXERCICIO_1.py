class Usuario:
    def __init__(self, primeironome, ultimonome):
        self.primeironome = primeironome
        self.ultimonome = ultimonome

    def hello(self):
        return f"Olá {self.primeironome} {self.ultimonome}"

    def set_nome(self, primeironome, ultimonome):
        self.primeironome = primeironome
        self.ultimonome = ultimonome

    def get_nome(self):
        return f"{self.primeironome} {self.ultimonome}"

# Create instances of the Usuario class
usuario1 = Usuario("Isaak", "Gomes")
usuario2 = Usuario("Paulo", "Cesar")

# Call the hello() method for each instance
print(usuario1.hello())
print(usuario2.hello())

# Change the name of usuario1 using the set_nome() method
usuario1.set_nome("João", "Santos")

# Call the get_nome() method to retrieve the new name of usuario1
print(usuario1.get_nome())
