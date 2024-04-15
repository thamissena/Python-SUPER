#Atividade 5:
class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0  # Inicialmente o valor total é zero

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade

# Criando uma instância da classe Fatura
fatura = Fatura("Produto A", 10, 3)
fatura.gerar_fatura()

print(f"Nome do item: {fatura.nome_item}")
print(f"Preço unitário: {fatura.preco_unitario}")
print(f"Quantidade: {fatura.quantidade}")
print(f"Valor total da fatura: {fatura.valor_total}")

#ATIVIDADE 3:

class Empresa:
    def __init__(self,nome):
        self.nome = nome
        self.funcionarios = [ ]

    def adicionarFun (self,funcionario):
        self.funcionarios.append(funcionario)

    def remover_funcionario(self,nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f'Funcionário {nome} removido com sucesso.')
            else:
                print('Funcionário não encontrado')
    def listar_funcioario(self):
        if self.funcionarios:
                for funcionario in self.funcionarios:
                    print(f"Nome: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")
        else:
            print("Não há funcionários nesta empresa.")

class Funcionario(Empresa):
    def __init__(self,nome,cargo,salario):
        self.nome = nome 
        self.cargo = cargo
        self.salario = salario
#if __name__ == "_ _main_ _":
# from aula11 import (Empresa, Funcionario)
nome_empresa = input("Digite o nome da empresa: ")
empresa = Empresa(nome_empresa)

while True:
    print('\nMenu:')
    print('1. Adicionar funcionário.')
    print('2. Remover funcionário. ')
    print('3. Listar funcionários.')
    print('4. Sair do programa.')

    opcao = input('Digite a opção desejada: ')

    if opcao == "1":
       nome = input('Digite o nome do funcionário: ')
       cargo = input('Digite seu cargo: ')
       salario = input('Digite seu salário: ')
       funcionarioadd = Funcionario(nome,cargo,salario)
       empresa.adicionarFun(funcionarioadd) 

    elif opcao == "2":
        empresa.listar_funcioario( )
        nome_funcionario = input("Digite o nome do funcionário a ser removido: ")
        empresa.remover_funcionario(nome_funcionario)
    elif opcao == "3":
       empresa.listar_funcioario( )
    elif opcao == "4":
            print("Saindo...")
            break
    else:
            print("Opção inválida. Tente novamente.")
exit( )
#ATIVIDADE 1:
class Cachorro:
    def __init__(self,nome,raca,idade):
        self.nome = nome
        self.raca =raca
        self.idade= idade

shitzu = Cachorro ('Bob','Shitzu',10)
print(type(shitzu))
print(shitzu.idade, shitzu.nome)






