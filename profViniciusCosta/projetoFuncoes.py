import os

linhas = 60

tarefas = {}


def limparTela():
    os.system("cls")


def geraCodigo() -> int:
    return len(tarefas) + 1


def adicionarTarefas():
    codigo = geraCodigo()
    nome = input("Digite o NOME da Tarefa: ").strip().upper()
    descricao = input("Digite a DESCRIÇÃO da Tarefa: ").strip().upper()
    prioridade = int( input("Digite a PRIORIDADE: ") )
    categoria = input("Digite a CATEGORIA ([N]ormal ou [U]rgente): ").strip().upper()
    concluida = False
    
    tarefas[codigo] = [nome, descricao, prioridade, categoria, concluida]


def marcarConcluida():
    for codigo, tarefa in tarefas.items():
        print(f"Código:{codigo}, Tarefa: {tarefa[0]} ")
    op = input("Informe o CÓDIGO da Tarefa Concluída: ").strip().upper()
    if int(codigo) in tarefas:
        tarefas [codigo] [4] = True
    


def listarTodas():
    for chave in tarefas:
        print( tarefas[chave])


def listarConcluidas():
    for chave in tarefas:
        if tarefas[chave][4]:
            print( tarefas[chave])


while True:
    print(
        f"""
            {'=' * linhas}
            1 - Adicionar Tarefas
            2 - Marcar como Concluída
            3 - Listar Todas as Tarefas
            4 - Listar por Prioridade
            5 - Listar por Categoria
            6 - Listar Concluídas
            {'.' * linhas}   
            S - Sair
            {'-' * linhas}   
        """
    )
    opcao = input('>>>: ').strip().upper()
    limparTela()

    match (opcao):
        case '1':
            adicionarTarefas()
        case '2':
            marcarConcluida()
        case '3':
            listarTodas()
        case '4':
            listarPrioridade()
        case '5':
            listarCategoria()
        case '6':
            listarConcluidas()
        case 'S':
            exit()
        case _:
            print("Opção Inválida!")
        
        