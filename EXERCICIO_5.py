class Usuario():
    def __init__(self, nome_usuario=""):
        self.__nome_usuario = nome_usuario

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, novo_nome):
        self.__nome_usuario = novo_nome

    def __str__(self):
        return f"Usuario({self.nome_usuario})"


class Admin(Usuario):
    def diga_ola(self):
        if self.nome_usuario:
            return f"Olá admin, {self.nome_usuario}"
        else:
            return "Olá admin, eu não sei o seu nome"


admin1 = Admin("Baltazar")
print(admin1.diga_ola())
print(admin1)

admin2 = Admin()
print(admin2.diga_ola())
print(admin2)
