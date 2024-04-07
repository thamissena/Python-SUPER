import sqlite3 as sql
from stringSQL import (comandoSQL, )
def abrirBanco():
    #Criar e Abrir o Banco de Dados(data base), caso ele não exista.
   conexao = sql.connect("Cadastro.db") # CREATE DATABASE IF NOT EXISTS Cadastro.db - "no SQL"
   return conexao
def criarTabelas (conexao):
    #Cursor ele cria uma ponte emtre a linguagem e o Bancp (SQL)
    cursor = conexao.cursor()
    # Método '.execute()', executa os comandos SQL
    # Criar Tabela Categorias:
    cursor.execute(comandoSQL[0])
    # Criar Tabela Produto:
    cursor.execute(comandoSQL[1])

def incluirCat():
    descricao = input("Informe a Descrição da Nova Categoria: ").upper().strip()
    conexao = abrirBanco ()
    cursor = conexao.cursor ()
    cursor.execute(comandoSQL[2], (descricao,))
    conexao.commit() #salvar informaçao nova no banco

def relCategoria():
    conexao = abrirBanco ()
    cursor = conexao.cursor ()
    cursor.execute(comandoSQL[4])
    listaCategorias = cursor.fetchall() #.fetchall formatar o dicionario em uma  lista em python
    print(listaCategorias)
    
def incluirProd():
    print('-'*60)
    relCategoria()
    print('-'*60)
    nomeprod = input("Imforme o nome do Produto: ").upper()
    codCat = int(input("Informe o Código da Categoria: "))
    preco = float(input("Informe o Preço do Produto: "))
    qt = int(input("Informe a Quatida de Produto: "))
    ativo = input("Produto ativo(S/N): ").upper().strip()
    ativo = True if (ativo =='s') else False
    conexao = abrirBanco ()
    cursor = conexao.cursor ()
    cursor.execute(comandoSQL[3], (nomeprod,codCat,preco,qt, ativo))
    conexao.commit()
    
def cadCategorias():
    menu = {
        '1':["Inclusão de Categorias", "incluirCat()"],
        '2':["Alteração de Categorias", "alterarCat()"],
        '3':["Exclusão de Categorias", "excluirCat()"],
        'R':["Retornar ao Menu Principal", " " ], #como o menu princial nao é uma funcao, então vai ser add um break para sair do loop de categoria, o exit sai do programa não é aplicavel.O 'break' vai como texto pq o eval já transforma como funcao.
    }
    while True:   
        print('='*60)
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao[0]}")
        print('-'*60)
        opcao = input("Informe uma das opções acima: ").upper().strip()
        if opcao.upper() == 'R':break
        eval(menu[opcao][1]) #transforma uma string em inteiro, ou transforma uma string em comando

def alterarCat():
    pass
def excluirCat():
    pass

def cadProdutos ():
    menu = {
        '1':["Inclusão de Produtos", "incluirProd()"],
        '2':["Alteração de Produtos", "alterarProd()"],
        '3':["Exclusão de Produtos", "excluirProd()"],
        'R':["Retornar ao Menu Principal", " " ],
    }
    while True:   
        print('='*68)
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao[0]}")
        print('-'*68)
        opcao = input("Informe uma das opções acima: ").upper().strip()
        if opcao.upper() == 'R':break
        eval(menu[opcao][1])

def alterarProd():
    pass
def excluirProd():
    pass
#---------
#contr+H ele aparece a box para substituir um valor para todo o  programa