from exemplo1 import (Carros, Motocicletas)

# Estanciar um objeto:
chevette = Carros("GM", "1980", 180)
opala = Carros("GM", "1984", 180, "Vermelho")
maverick = Carros("Ford", "1976", 220, "Azul")

print( "Chevette Ligado? ", chevette.ligado)    # False
chevette.ligarDesligar()
print( "Chevette Ligado? ", chevette.ligado)    # True
for a in range(19):
    chevette.acelerar()
    print("velocidade Chevette = ", chevette.veloAtual)

print( type(chevette) )

for k, v in (chevette.__dict__).items():
    print(k, v)

carro1 = Carros.__new__
  
texto = "infinity"
print( type( texto))
texto.upper()

cg150 = Motocicletas(ano="2020", marca="Honda", maxima=160, cor="Vermelha")
print(cg150.veloAtual )  # 0
cg150.ligarDesligar()
cg150.acelerar()
print(cg150.veloAtual )     # 10
