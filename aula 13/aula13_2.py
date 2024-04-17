#Atividade 5:
class ContasCorrentes:
    def __init__(self, numero, correntista):
        self.numero = numero
        self.correntista = correntista
        self.__saldo = 0 
        
    #Decorator (Disfarce)
    @property
    def movimentar(self):   #Getter
        return f"R$ {self.__saldo}"

    @movimentar.setter    #Setter
    def movimentar(self,valor):
        if(self.__saldo + valor) >= 0:
            self.__saldo += valor
        else:
          print ("Saldo depositado negativo.")
# Para ter um Setter precisa de um Getter, mas podemos fazer um Getter sem o Setter.   
#####################################################
minhaConta = ContasCorrentes("12345-0","Vinicius Costas")
print(f"Número da conta: {minhaConta.numero}") 
print(minhaConta.movimentar)  #Getter -> 0 

minhaConta.movimentar = -100  #Setter

print (minhaConta.movimentar)  #Getter - > - 100 (não pode)

minhaConta.movimentar = 100  #Setter

print (minhaConta.movimentar)  #Getter - > 100 
#------------------------------------------------
exit()

#Atividade 1:
class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        print(f"Tarefas do projeto '{self.nome}':")
        for tarefa in self.tarefas:
            print(f"- {tarefa.nome}: {tarefa.descricao}")

# Exemplo de uso:
projeto = Projeto("Projeto A")

tarefa1 = Tarefa("Tarefa 1", "Concluir relatório")
tarefa2 = Tarefa("Tarefa 2", "Enviar e-mails para clientes")
tarefa3 = Tarefa("Tarefa 3", "Realizar reunião de equipe")

projeto.adicionar_tarefa(tarefa1)
projeto.adicionar_tarefa(tarefa2)
projeto.adicionar_tarefa(tarefa3)

projeto.listar_tarefas()