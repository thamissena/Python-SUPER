class Veiculos:
    pass


class Carros(Veiculos):
    # Método Especial(Construtor)
    # DUNDER (Double UNDERline)
    def __init__(self, marca, ano, maxima, cor="Branca"):    
        self.marca = marca
        self.modelo = ano
        self.cor = cor
        self.veloMax = maxima
        self.veloAtual = 0
        self.ligado = False
    
    def acelerar(self):
        if self.ligado:
            if (self.veloAtual + 10) <= self.veloMax:
                self.veloAtual += 10
            else:
                self.veloAtual = self.veloMax

    def frear(self):
        if (self.veloAtual - 10) >= 0:
            self.veloAtual -= 10
        else:
            self.veloAtual = 0
    
    def ligarDesligar(self):
        if self.veloAtual == 0:
            self.ligado = not self.ligado
        else:
            if not self.ligado:
                self.ligado = True    


class Triciclos:
    pass


# Mãe -> Filha
# Super Classe -> Sub Classe
class Motocicletas(Carros, Triciclos):  
    def __init__(self, marca, ano, maxima, cor="Branca", descansoLateral = True):
        Carros.__init__(self, marca, ano, maxima, cor)
        self.descansoLateral = descansoLateral
                