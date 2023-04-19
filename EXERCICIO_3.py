class Usuario:
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

    def hello(self):
        return f"Olá {self.primeiro_nome} {self.ultimo_nome}"

usuario1 = Usuario("Joe", "")
print(usuario1.hello())


class Empregado():
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.salario = salario
        self.projeto = projeto

    def trabalho(self):
        return f"O funcionario(a) {self.nome} está trabalhando no projeto {self.projeto}"

    def mostrar(self):
        return f"Funcionario: {self.nome}, Salário: {self.salario}"

funcionario1 = Empregado("João", 100, "Fabrica de Software")
print(funcionario1.trabalho())
print(funcionario1.mostrar())


class Robo():
    def __init__(self, nome, ano_construcao):
        self.nome = nome
        self.ano_construcao = ano_construcao

    def diga_alo(self):
        return f"Nome do robo: {self.nome}, Ano de construção: {self.ano_construcao}"

robo1 = Robo("Atlas", "1500")
print(robo1.diga_alo())


class Laptop():
    def __init__(self, preco):
        self.preco = preco

laptop1 = Laptop("3999")
print(laptop1.preco)


class Pessoa():
    def __init__(self, primeiro_nome, ultimo_nome):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome

    def nome_completo(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"

pessoa1 = Pessoa("João", "Carvalho")
print(f"Meu nome é {pessoa1.nome_completo()}")
#exercicio 3
