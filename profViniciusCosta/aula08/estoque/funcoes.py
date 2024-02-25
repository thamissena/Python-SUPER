from geral import (banco, )

def geraCodigo():
    if len(banco)==0:
        return 1
    else:
        return len(banco)+1


def incluir():
    while True:
        nome = input("Digite NOME do Produto: ").strip().upper()
        preco = float( input("Digite o PREÇO do Produto: ") )
        qt = int( input("Digite a QUANTIDADE: ") )
        categoria = input("Digite a CATEGORIA: ").upper().strip()
        banco[geraCodigo()] = [nome, preco, qt, categoria]
        escolha = input("Continuar a incluir (S/N)?").strip().upper()
        if escolha != 'S': break

def listaGeral():
    print( banco )

def alterar():
    