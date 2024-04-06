alunos = { }

def AdicionarAluno(nome, nmatricula):
    alunos[nmatricula] = nome

def VerAlunos():
  if not alunos: 
    print ("\nNenhum aluno registrado.")
  else:
    print("\n LISTA DE ALUNOS:")
    for nmatricula, nome in alunos.items(): 
       print(f"Nome de aluno: {nome}, Matrícula:{nmatricula}")
   
def RemoverAluno(alunoremove): 
    if alunoremove in alunos:
       del alunos[alunoremove] 
       print("Aluno removido com sucesso.") 
    else:
       print("Aluno não encontrado.")

def AtualizarAluno(alunoatualiza):
    if alunoatualiza in alunos:
       novonome = input(f"\nDigite o novo nome do aluno para a matrícula {alunoatualiza}: ")
       alunos[alunoatualiza]= novonome
    else:
      print("\nAluno não encontrado.") 
 