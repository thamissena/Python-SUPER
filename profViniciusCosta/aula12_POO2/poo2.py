class Carros:
    # Método Construtor:
    def __init__(self, maxima, cor="Branca"):
        # Atributos:
        self.cor = cor
        self.veloMax = maxima

    def frear(self):
        return f"Freando..."

class Caminhoes(Carros):
    pass

# Estanciando objeto:
objCaminhao = Caminhoes(cor="Vermelha", maxima=190)

print( objCaminhao.frear() )
