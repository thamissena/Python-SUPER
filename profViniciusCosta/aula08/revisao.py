def palindromo(texto):
    return ( True if texto == texto[::-1] else False)

print( palindromo("ana") )   # True
print( palindromo("joao") )  # False

print("Infinity School"[::-1])
print("Infinity School"[0:9])

endereco = "Rua ABC, 123"
temNumero = [c.isdigit() for c in endereco]
if any(temNumero):
    print("Não digite o número no ENDEREÇO!")
if all(temNumero):
    print("Todos os Caracteres são Números")
else:
    print("Nem Todos os Caracteres são Números")

exit()


conjuntoCores = {"Azul", "Vermelho", "Verde", "Branco", "Rosa"}

def maior4(conjunto):
    listaRetorno = []
    for cor in list(conjunto):
        if len(cor)>4:
            listaRetorno.append(cor)
    return listaRetorno

print( maior4(conjuntoCores) )






exit()

import random as rd

lista = [ rd.randint(1,100) for v in range(1000) ]
for v in lista:
    if (v%2) == 0:
        print(v, end=' - ')