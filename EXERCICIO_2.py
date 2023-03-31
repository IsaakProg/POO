import datetime

class Usuario:
    def __init__(self, primeiro_nome, ultimo_nome, data_nascimento):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.data_nascimento = data_nascimento

    def hello(self, pessoa):
        return f"Olá {pessoa.primeiro_nome} {pessoa.ultimo_nome}, meu nome é {self.primeiro_nome}"

    def calcular_idade(self):
        data_atual = datetime.date.today()
        idade = data_atual.year - self.data_nascimento.year
        if data_atual.month < self.data_nascimento.month or \
           (data_atual.month == self.data_nascimento.month and data_atual.day < self.data_nascimento.day):
            idade -= 1
        return idade


usuario1 = Usuario("Isaak", "Gomes", datetime.date(1998, 6, 15))
usuario2 = Usuario("Pedro", "Henrique", datetime.date(2000, 10, 3))

# Usuario1 dando olá para o usuario2 e vice e versa
print(usuario1.hello(usuario2))
print(usuario2.hello(usuario1))

# Calculando as idades dos usuários
print(usuario1.calcular_idade())
print(usuario2.calcular_idade())
