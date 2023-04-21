# 1.Hierarquia de classes para animais:


class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

class Peixe(Animal):
    def falar(self):
        return "Glub glub!"
    
#Para demonstrar o polimorfismo, basta criar instâncias de cada subclasse e chamar o método falar() em cada uma delas:


animal = Animal()
cachorro = Cachorro()
gato = Gato()
peixe = Peixe()

print(animal.falar())    # não faz nenhum som
print(cachorro.falar())  # Au au!
print(gato.falar())      # Miau!
print(peixe.falar())     # Glub glub!

# 2.Classes Animal, Cachorro e Gato:


class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.falar())

# 3.Classes Carro, CarroGasolina e CarroEletrico:


class Carro:
    def dirigir(self):
        pass

class CarroGasolina(Carro):
    def dirigir(self):
        return "Dirigindo carro a gasolina"

class CarroEletrico(Carro):
    def dirigir(self):
        return "Dirigindo carro elétrico"

def testar_carros(carro):
    print(carro.dirigir())

carro_gasolina = CarroGasolina()
carro_eletrico = CarroEletrico()

testar_carros(carro_gasolina)
testar_carros(carro_eletrico)

# 4.Classes Forma, Circulo e Quadrado:


from math import pi

class Forma:
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return pi * self.raio ** 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

formas = [Circulo(2), Quadrado(3)]

for forma in formas:
    print(forma.area())

# 5.Classes Empregado, EmpregadoHora e EmpregadoMes:

class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def pagar_salario(self):
        raise NotImplementedError("Subclass deve implementar o método pagar_salario.")

class EmpregadoHora(Empregado):
    def __init__(self, nome, salario_hora, horas_trabalhadas):
        super().__init__(nome, salario_hora)
        self.horas_trabalhadas = horas_trabalhadas
    
    def pagar_salario(self):
        return self.salario * self.horas_trabalhadas

class EmpregadoMes(Empregado):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome, salario_mensal)
    
    def pagar_salario(self):
        return self.salario

# Criando a lista de empregados
empregados = [EmpregadoHora("João", 20, 160), EmpregadoMes("Maria", 2000)]

# Iterando sobre a lista e chamando o método pagar_salario de cada funcionário
for empregado in empregados:
    print(f"{empregado.nome} recebeu R${empregado.pagar_salario()} de salário.")

# 6.Classes Conta Bancaria, ContaCorrente e ContaPoupanca:

class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.05):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def adicionar_juros(self):
        self.saldo += self.saldo * self.taxa_juros

class ContaCorrente(ContaBancaria):
    def __init__(self, saldo=0, taxa_juros=0.02):
        super().__init__(saldo)
        self.taxa_juros = taxa_juros

    def adicionar_juros(self):
        self.saldo += self.saldo * self.taxa_juros

conta_poupanca = ContaPoupanca(1000)
conta_poupanca.adicionar_juros()
print(conta_poupanca.saldo) # Exibe 1050.0

conta_corrente = ContaCorrente(500)
conta_corrente.adicionar_juros()
print(conta_corrente.saldo) # Exibe 510.0


