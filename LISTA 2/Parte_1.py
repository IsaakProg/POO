# EXERCICIO 1

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir_info(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")
        
class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
        
    def imprimir_info(self):
        super().imprimir_info()
        print(f"Nota: {self.nota}")


#EXERCICIO 2

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def imprimir_info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")
        
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, qtd_portas):
        super().__init__(marca, modelo, ano)
        self.qtd_portas = qtd_portas
        
    def imprimir_info(self):
        super().imprimir_info()
        print(f"Quantidade de portas: {self.qtd_portas}")
        
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        
    def imprimir_info(self):
        super().imprimir_info()
        print(f"Cilindradas: {self.cilindradas}")


#EXERCICIO 3

class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        
    def comer(self):
        print("Comendo...")
        
class Cachorro(Animal):
    def latir(self):
        print("Au au!")
        
class Gato(Animal):
    def miar(self):
        print("Miau!")


#EXERCICIO 4

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
        
    def aumento(self, porcentagem):
        self.salario += self.salario * porcentagem / 100


#EXERCICIO 5

import math

class Forma:
    def area(self):
        pass
    
class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    def area(self):
        return self.comprimento * self.largura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        return math.pi * self.raio ** 2
