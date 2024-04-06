
"""Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
Para isso, você deve implementar um módulo que contém as seguintes funções:
AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
Lembre Se de Modularizar o código"""

from funcoesdicionario import *

print ("\n DICIONÁRIO DE ALUNOS")
while True:
    print("\nMenu:")
    print("1. ADICIONAR aluno")
    print("2. REMOVER aluno")
    print("3. ATUALIZAR aluno")
    print("4. VISUALIZAR todos alunos")
    print("5. Fechar dicionário")
    opcao = input ("\n Digite o número correspondente no que deseja realizar: ")
     
    if opcao=="1":
        print("\nAdicionar aluno:")
        nomealuno = input("Insira o nome do aluno: ")
        matricula = input("Insira o número de matrícula composto apenas por dígititos numericos sem caracteres): ")
        AdicionarAluno(nomealuno,matricula)
        print("\nAluno adicionada com sucesso!")
    elif opcao == "2":
       if not alunos:
            print ("\nNenhum aluno registrado.")
       else:
        VerAlunos()
        alunoremovido = input("\nDigite o número de matrícula do aluno que deseja remover: ")
        RemoverAluno(alunoremovido)
    elif opcao == "3":
       if not alunos:
           print ("\nNenhum aluno registrado.")
       else:
          VerAlunos()
          atulizado = input("\nDigite o número de matrícula do aluno que desejar atualizar: ")
          AtualizarAluno(atulizado)
          print("\nAluno atualizado com sucesso.")         
    elif opcao == "4":
       VerAlunos()
    elif opcao == "5":
       break
    else:
       print("Opçao não encontrada.")