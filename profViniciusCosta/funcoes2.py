print(True == 1)

def somarNumeros(*numeros):
    listaNumeros = []
    for valor in numeros:
        listaNumeros.append( isinstance( valor, float ) )
    if not all(listaNumeros):
        return f"Argumentos NÃO podem ser String!!"
    soma = 0
    for num in numeros:
        soma += num
        # soma = soma + num
    return soma
    
# Programa:
var1=''
while not isinstance(var1, float):
    var1 = input("Digite PRIMEIRO Número: ")
var2 = float( input("Digite SEGUNDO Número: "))
print( f"Soma é { somarNumeros(var1, var2) }" )
print( f"Soma2 é { somarNumeros(var1, var2, 100.0) }" )
print( f"Soma3 é { somarNumeros(var1, var2, '100') }" )


exit()
'''
    Revisão Aula 1 - Funções:
'''

def media(n1, n2, n3) -> float:
    """
        Esta função calcula a Média Aritmética das notas do Estudante
        Entrada: 3 valores float
        Saída: Valor (escalar) das médias das Notas (Float)
    """
    listaValores = n1,n2,n3
    
    return sum( listaValores ) / len(listaValores)

#-------------------------------------------------------------------------------
# App:
notas = list() 
for indice in range(3):
    notas.append( float( input(f"Digite a nota da prova {indice+1}: ") ) )
listaNotasTexto = [ str(nota) for nota in notas ]
a,b,c = notas
print(f"Sua Média foi { media(a,b,c) } nas Notas: {' , '.join(listaNotasTexto)}")