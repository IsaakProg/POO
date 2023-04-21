class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Coordenadas do ponto: ({self.x}, {self.y})"
    
    def distancia(self, outro_ponto):
        return ((self.x - outro_ponto.x) ** 2 + (self.y - outro_ponto.y) ** 2) ** 0.5


class Retangulo:
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

    def centro(self):
        x_centro = self.ponto_inicial.x + self.largura/2
        y_centro = self.ponto_inicial.y + self.altura/2
        return Ponto(x_centro, y_centro)
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def ponto_dentro(self, ponto):
        if self.ponto_inicial.x <= ponto.x <= self.ponto_inicial.x + self.largura \
        and self.ponto_inicial.y <= ponto.y <= self.ponto_inicial.y + self.altura:
            return True
        else:
            return False


ponto1 = Ponto(0, 0)
retangulo1 = Retangulo(5, 3, ponto1)

ponto2 = Ponto(2, 2)
retangulo2 = Retangulo(4, 6, ponto2)

opcao = 0

while opcao != 4:
    print("Escolha uma opção:")
    print("1 - Alterar valores do retângulo 1")
    print("2 - Alterar valores do retângulo 2")
    print("3 - Verificar se um ponto está dentro de um retângulo")
    print("4 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        largura = float(input("Nova largura do retângulo 1: "))
        altura = float(input("Nova altura do retângulo 1: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 1: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 1: "))

        ponto1 = Ponto(x, y)
        retangulo1 = Retangulo(largura, altura, ponto1)

        centro_retangulo1 = retangulo1.centro()
        print(f"Centro do retângulo 1: {centro_retangulo1}")
        print(f"Área do retângulo 1: {retangulo1.area()}")
        print(f"Perímetro do retângulo 1: {retangulo1.perimetro()}")

    elif opcao == 2:
        largura = float(input("Nova largura do retângulo 2: "))
        altura = float(input("Nova altura do retângulo 2: "))
        x = float(input("Nova coordenada x do ponto inicial do retângulo 2: "))
        y = float(input("Nova coordenada y do ponto inicial do retângulo 2: "))
