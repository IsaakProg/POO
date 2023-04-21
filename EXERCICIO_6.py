class Usuario:
    pontos = 0
    numeroDeArtigos = 0
    
    def setNumeroDeArtigos(self, nart):
        self.numeroDeArtigos = nart
    
    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao(self):
        pass
        
class Autor(Usuario):
    
    def calcPontuacao(self):
        return self.numeroDeArtigos * 10 + 20
    
class Editor(Usuario):
    
    def calcPontuacao(self):
        return self.numeroDeArtigos * 6 + 15

# criando objeto autor1
autor1 = Autor()
autor1.setNumeroDeArtigos(8)

# imprimindo pontuações obtidas pelo autor1
print("Pontuação do autor1: ", autor1.calcPontuacao())

# criando objeto editor1
editor1 = Editor()
editor1.setNumeroDeArtigos(15)

# imprimindo pontuações obtidas pelo editor1
print("Pontuação do editor1: ", editor1.calcPontuacao())
