import random

class Bichinho:
    def __init__(self, nome, fome, saude, idade, tedio):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio

    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fome: {self.fome}
        Saúde: {self.saude}
        Idade: {self.idade}
        Tédio: {self.tedio}
        """

    def humor(self):
        return (self.fome + self.saude) / 2

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        self.saude += quantidade_comida / 2

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0
        self.saude += tempo_brincadeira / 2

    def dormir(self):
        self.fome += 1
        self.saude += 2
        self.idade += 1


class FazendaDeBichinhos:
    def __init__(self, quantidade_bichinhos):
        self.bichinhos = []
        for i in range(quantidade_bichinhos):
            nome = f"Bichinho{i}"
            fome = random.randint(0, 10)
            saude = random.randint(0, 10)
            idade = random.randint(0, 10)
            tedio = random.randint(0, 10)
            bichinho = Bichinho(nome, fome, saude, idade, tedio)
            self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade_comida)

    def brincar_todos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo_brincadeira)

    def dormir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.dormir()

    def mostrar_bichinhos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

fazenda = FazendaDeBichinhos(3)

opcao = 0

opcao = 0

while opcao != 5:
    print("----- CUIDANDO DA FAZENDA DE BICHINHOS -----")
    print("1 - Alimentar todos os bichinhos")
    print("2 - Brincar com todos os bichinhos")
    print("3 - Fazer todos os bichinhos dormir")
    print("4 - Mostrar todos os bichinhos")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        quantidade_comida = int(input("Quantidade de comida a dar para cada bichinho: "))
        fazenda.alimentar_todos(quantidade_comida)
    elif opcao == 2:
        tempo_brincadeira = int(input("Tempo de brincadeira (em horas): "))
        fazenda.brincar_todos(tempo_brincadeira)
    elif opcao == 3:
        fazenda.dormir_todos()
    elif opcao == 4:
        fazenda.mostrar_bichinhos()
    elif opcao == 42: # opção secreta para mostrar os valores exatos dos atributos do objeto
        print("Valores exatos dos atributos dos bichinhos:")
        for bichinho in fazenda.bichinhos:
            print(bichinho.__dict__)
    elif opcao == 5:
        print("Até mais!")
    else:
        print("Opção inválida. Escolha novamente.")
