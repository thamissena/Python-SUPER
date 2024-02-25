def somar(*args:float) -> float:
    """
        Esta função SOMA qq quantidade de valores.
        *args: Lista de valores
        retorna: somatório dos valores da lista
    """
    return sum(args)


def subtrair(*listaValores:float) -> float:
    """
        Esta função SUBTRAI qq quantidade de valores.
        *args: Lista de valores
        retorna: somatório dos valores da lista
    """
    valorInicial = listaValores[0]
    for indice in range(1, len(listaValores) ):
        valorInicial -= listaValores[indice]
    return valorInicial

#print( list( filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8,9]) ) )


from functools import (reduce,)
def multiplicar(*listaValores):
    """
        produto = 1
        for valor in valores:
            produto *= valor
        return produto
    """
    return reduce(lambda valor, produto=1: valor*produto, listaValores)


def dividir(a,b):
    return (a/b if b != 0 else None)
