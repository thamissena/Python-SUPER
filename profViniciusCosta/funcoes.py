"""
    Funções em Python
"""
# 05) Escreva uma função que receba um nome
#  como parâmetro e informe quantas vogais
#  existem nele.

# 12) Faça um programa que receba um número
#  por parâmetro e apresente em tela a
#  seguinte impressão:
#  1
#  2 2
#  3 3 3
#  .
#  .
#  .
#  n n n n n
def somar(n1, n2):
    return (n2+n1)
def subtrair(n1, n2):
    return (n1-n2)
def multiplicar(n1, n2):
    return (n1*n2)
def dividir(n1, n2):
    return (n1/n2)

# Programa:
linha = 60
while True:
    print("=" * linha)
    print("1 - Somar Valores")
    print("2 - Subtrair Valores")
    print("3 - Multiplicar Valores")
    print("4 - Dividir Valores")
    print("." * linha)
    print("S - Sair")
    print("-" * linha)
    opcao = input(': ').strip().upper()
    if opcao == 'S': break
    valor1 = float( input("Informe: ") )
    valor2 = float( input("Informe: ") )
    r = "Resultado: "
    match(opcao):
        case '1':
          print( r , somar(valor1, valor2) ) 
        case '2':
          print( r , subtrair(valor1, valor2)  )
        case '3':
          print( r , multiplicar(valor1, valor2)  )
        case '4':
          print( r , dividir(valor1, valor2)  )
        case _:
          print("Opção inválida!")
    input("Pressione qq tecla p/continuar...")
exit()

# --------------------------------
import datetime as dt

result = dt.datetime.now().hour
print("result:", result)



def saudacao2(nome:str, hora:int) -> str:
    """
        Função de saudação persomalizada
        Entrada =   nome: Nome do Usuário
                    hora: Inteiro representando a hora do dia
        Saída = String concatenada
    """
    if hora < 13:
        return f"Olá {nome}, Bom Dia!"
    elif hora < 18:
        return f"Olá {nome}, Bom Tarde!"
    else:
        return f"Olá {nome}, Bom Noite!"
    
# Programa:
nome = input("Informe seu NOME: ").strip().upper()
h = int( input("Informe a hora [0 á 24]: ") )
print( saudacao2( nome, h) )

exit()

def somar(x, y):
    return x+y

def media(n1, n2):
    return somar(n1, n2)/2

print( media(1,3) )

imprimir = print
imprimir(1+2) 

def saudacao() -> str:
    """
        Esta Rotina (Procedimento) imprime uma saudação padrão
        Args: None
        Retorno: String: 'Olá'
    """
    return f"Olá"
    print('')

print( saudacao() )


exit()
# Revisão:
minhaLista = [1, True, "String", 3.14]

minhaTupla = (1,2,3,4)

meuDic = {
    1: "Texto 1",
    2: "Texto 2",
    3: "Texto 3",
}

meusContatos = {
    ["Vinicius Costa", True, "999.888.777"],
    ["Vinicius Costa", True, "999.888.777"],
    ["Vinicius Costa", True, "999.888.777"],

}

