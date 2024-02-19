cadastro = dict( )
print ('\n Alunos matriculados.')
while True:
   opcao = input ('Digite 1 para cadastras um aluno(a), 2 para remove, 3 para visualizar os alunos cadastrados e 0 para sair do programa:  ')
   if opcao == '0': 
      print('\nPrograma encerrado.')
      break
   if opcao== '1':
      aluno = input("Digite o nome do aluno(a): ") 
      matricula = input('Digite o número de matrícula: ')
      cadastro[aluno]={matricula}
   if opcao == '2':
      removido = input('Digite o nome do aluno(a) que deseja remover: ')
      del(cadastro[removido])
   else:
      for aluno, matricula in cadastro.items( ):
         print(f'{aluno}: {matricula}')