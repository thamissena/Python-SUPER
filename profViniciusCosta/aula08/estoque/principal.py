from geral import (linhas, )
from funcoes import (incluir, listaGeral )

while True:
    print("-" * linhas)
    print("1 - Inclusão")
    print("2 - Alteração")
    print("3 - Exclusão")
    print("4 - Listagem Geral")
    print("." * linhas)
    print("S - Sair")
    print("-" * linhas)

    opcao = input(': ').upper().strip()

    match(opcao):
        case '1':
            incluir()
        case '2':
            pass
            #alterar()
        case '3':
            pass
            #excluir()
        case '4':
            listaGeral()
        case 'S':
            exit()
        case _:
            print("Opção Inválida!!")