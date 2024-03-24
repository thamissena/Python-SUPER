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
    print("Função de Inclusão de Categorias!!!")
    
def incluirProd():
    print("Função de Inclusão de Produtos!!!")    
    
def cadCategorias():
    menu = {
        '1':["Inclusão de Categorias", "incluirCat()"],
        '2':["Alteração de Categorias", "alterarCat()"],
        '3':["Exclusão de Categorias", "excluirCat()"],
    }
    while True:   
        print('='*68)
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao[0]}")
        print('-'*68)
        print("S - Sair para Menu Principal")
        print('-'*68)
        opcao = input("Informe uma das opções acima: ").upper().strip()
        eval(menu[opcao][1]) #transforma uma string em inteiro, ou transforma uma string em comando

def cadProdutos ():
    menu = {
        '1':["Inclusão de Produtos", "incluirCat()"],
        '2':["Alteração de Produtos", "alterarCat()"],
        '3':["Exclusão de Produtos", "excluirCat()"],
    }
    while True:   
        print('='*68)
        for opcao, descricao in menu.items():
            print(f"{opcao} - {descricao[0]}")
        print('-'*68)
        print("S - Sair para Menu Principal")
        print('-'*68)
        opcao = input("Informe uma das opções acima: ").upper().strip()
        eval(menu[opcao][1])