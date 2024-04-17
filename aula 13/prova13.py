class bombaCombustível: 
    
    def __init__(self, tipoCombustivel, valorLitro, quantidaCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidaCombustivel
    
    def abastecerPorValor(self, valor):
        litro_abastecido = valor / self.valorLitro 
        if litro_abastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel = self.quantidadeCombustivel - litro_abastecido
            print (f"Foi abestecido R$ {valor}, igual a {litro_abastecido:.2f} L de combustível.")
        else:
           print(f"Não há combustível suficiente na bomba.\nQuantidade de combustível na bomba = {self.quantidadeCombustivel} L.")
    
    def abastecerPorLitro(self,litros):
        valor_pagar = litros * self.valorLitro 
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel = self.quantidadeCombustivel - litros
            print (f"Foi abestecido {litros} L , igual a R$ {valor_pagar:.2f} a ser pago.")
        else:
            print(f"Não há combustível suficiente na bomba.\nQuantidade de combustível na bomba = {self.quantidadeCombustivel} L.")

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor
        
    def alterarCombustivel(self, novoTipCombustivel):
        self.tipoCombustivel = novoTipCombustivel

    def alterarQuantidadeCombustivel(self, novaQtdCombustivel):
        self.quantidadeCombustivel = novaQtdCombustivel

#exemplo
Bomba = bombaCombustível ("Gasolina", 5.58,1000)

Bomba.abastecerPorLitro(50)
Bomba.abastecerPorValor(340)
Bomba.alterarValor(10)
Bomba.abastecerPorLitro(10)
Bomba.abastecerPorLitro(500)
Bomba.alterarQuantidadeCombustivel(500)
Bomba.abastecerPorLitro(600)