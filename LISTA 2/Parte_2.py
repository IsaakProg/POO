#EXERCICIO 6

class ContaCorrente():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self._saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, cliente, saldo_minimo):
        super().__init__(numero, saldo, cliente)
        self._saldo_minimo = saldo_minimo

    def atualizar_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    @property
    def saldo_minimo(self):
        return self._saldo_minimo


class ContaEspecial(ContaCorrente):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.limite = limite


class ContaInvestimento(ContaCorrente):
    def __init__(self, numero, saldo, cliente, periodo, data_investimento):
        super().__init__(numero, saldo, cliente)
        self.data_investimento = data_investimento
        self.periodo = periodo


cliente1 = ContaCorrente("1234", 1000, "José")
cliente2 = ContaEspecial("4321", 1000, "Ana", 2000)
cliente3 = ContaPoupanca("4567", 1000, "João", 50)
cliente4 = ContaInvestimento("7654", 1000, "Pedro", "1 ano", "10/04/20203")

cliente1.depositar(1000)
print(cliente1.saldo)
cliente2.depositar(1000)
print(cliente2.saldo)
print(cliente3.saldo_minimo)


#EXERCICIO 7

class Empregado():
    def __init__(self, codigo, nome, email, salario):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    def aumento_salarial(self, porcentagem):
        self._salario += ((self._salario * porcentagem) / 100)


class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.beneficio = beneficio

    def aumento_salarial(self, porcentagem):
        super().aumento_salarial(porcentagem)
        self._salario += self.beneficio


class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.desconto = desconto

    def aumento_salarial(self, porcentagem):
        super().aumento_salarial(porcentagem)
        self._salario -= self.desconto


chefe1 = Chefe("1234", "José", "jose@gmail.com", 5000, 500)
estagiario1 = Estagiario("4321", "João", "joão@gmail.com", 2000, 200)


print(chefe1.salario)
print(estagiario1.salario)
chefe1.aumento_salarial(10)
estagiario1.aumento_salarial(10)
print(chefe1.salario)
print(estagiario1.salario)

#EXERCICIO 8

class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor}"


class Vip(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor + self.adicional}"


class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def __str__(self):
        return "Ingresso Normal"


class CamaroteInferior(Vip):
    def __init__(self, localizacao, valor, adicional):
        super().__init__(valor, adicional)
        self.localizacao = localizacao


class CamaroteSuperior(Vip):
    def __init__(self, valor, adicional, taxa_camarote, localizacao):
        super().__init__(valor, adicional)
        self.taxa_camarote = taxa_camarote
        self.localizacao = localizacao

    def imprime_valor(self):
        return f"Valor do ingresso: R$ {self.valor + self.adicional + self.taxa_camarote}"


ingresso_vip = Vip(100, 50)
ingresso_normal = Normal(100)
ingresso_camarote_inferior = CamaroteInferior("Camarote_1", 100, 50)
ingresso_camarote_superior = CamaroteSuperior(100, 50, 100, "Camarote_2")


print(ingresso_vip.imprime_valor())
print(ingresso_normal.imprime_valor())
print(ingresso_camarote_inferior.imprime_valor())
print(ingresso_camarote_superior.imprime_valor())

#EXERCICIO 9

class Funciario():
    def __init__(self, nome, endereco, telefone, email, salario):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome}, Endereço: {self.endereco}, Telefone: {self.telefone}, Email: {self.email}"


class Assistente(Funciario):
    def __init__(self, nome, endereco, telefone, email, matricula, salario):
        super().__init__(nome, endereco, telefone, email, salario)
        self.matricula = matricula


class AssistenteTecnico(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, salario, bonus):
        super().__init__(nome, endereco, telefone, email, matricula, salario)
        self.bonus = bonus


class AssistenteAdministrativo(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, salario, turno):
        super().__init__(nome, endereco, telefone, email, matricula, salario)
        self.turno = turno


assistente_tecnico1 = AssistenteTecnico(
    nome="João", endereco="Rua 1", telefone="123456789", email="joão@gmail.com", matricula="123", salario=1000, bonus=100)
assistente_administrativo1 = AssistenteAdministrativo(
    nome="Maria", endereco="Rua 2", telefone="987654321", email="maria@gmail.com", matricula="456", salario=1000, turno="Manhã")

print(f"Nome: {assistente_tecnico1.nome}, Matricula: {assistente_tecnico1.matricula}, Bonus: {assistente_tecnico1.bonus}")
print(f"Nome: {assistente_administrativo1.nome}, Matricula: {assistente_administrativo1.matricula}, Turno: {assistente_administrativo1.turno}")

#EXERCICIO 10

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro

    def faz_compras(self):
        print("Pessoa rica esta fazendo compras")


class Pobre(Pessoa):
    def trabalha(self):
        print("Pessoa pobre esta trabalhando")


class Miseravel(Pessoa):
    def mendiga(self):
        print("Pessoa miseravel esta mendigando")


pessoa_rico = Rica("João", 20, 1000)
pessoa_pobre = Pobre("Maria", 30)
pessoa_miseravel = Miseravel("José", 40)

pessoa_rico.faz_compras()
pessoa_pobre.trabalha()
pessoa_miseravel.mendiga()

