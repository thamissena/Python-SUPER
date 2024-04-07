# Baixou a biblioteca sqlite "pip install db-sqlite3"; visualizar a biblioteca "pip list". instalar a extenção SQLIDE visuon
from funcoes import (cadCategorias, cadProdutos,abrirBanco,criarTabelas)

criarTabelas(abrirBanco())

while True:
    print('='*68)
    print("1 - Cadastro de Categorias")
    print("2 - Cadastro de Produtos")
    print('-'*68)
    print("S - Sair do Sistema")
    print('-'*68)
    opcao = input("Informe uma das opções acima: ").upper().strip()
    
    match (opcao):
        case '1':
            cadCategorias()
        case '2':
            cadProdutos()
        case 'S':
            exit ()
        