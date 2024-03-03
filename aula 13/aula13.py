class Clientes:
    def __init__(self, nome, endereco = None) -> None: #não entendi
        self.nome = nome
        self.endereco = endereco
        self.pedidos = []

    # def mostraPedido... como criar mais de um cliente 
    
class Pedidos:
    def __init__(self, numeroPedido, descricao)-> None:
        self.numero = numeroPedido
        self.descricao = descricao
        self.cliente = None



#-----------------------------------------------------------

objPedido1 = Pedidos(1, "Mémoria RAM 8GB")
objPedido2= Pedidos(3, "SSD 35000 1TB")
objPedido3= Pedidos(7,"Gabinete Micro Cubo")
objPedido4 = Pedidos(8,"Mémoria RAM 32GB")

objCliente = Clientes("Ana Carla", "Rua ABC, 123")
objCliente.pedidos.append(objPedido1)
objCliente.pedidos.append(objPedido2)

objCliente2 = Clientes("João Paulo","Rua Armalina, 197")
objCliente2.pedidos.append(objPedido3)
objCliente2.pedidos.append(objPedido4)

#Listagem:

for pedido in objCliente.pedidos :
    print(pedido.descricao)

#Insira o cliente no pedido:
objPedido1.cliente = objCliente
print(objPedido1.cliente.nome)

exit()

class Projetos:
    def __init__(self, codigoProjeto, descricao):
        self.codigo = codigoProjeto
        self.descricao = descricao
        self.tarefas = []

class Tarefas:
    def __init__ (self, descricao, numero):
        self.descricao = descricao
        self.numero = numero



#--------------------------------
objTarefa1 = Tarefas("Comprar passagem", 1)
objTarefa2 = Tarefas("Arrumar malas", 2)

objProjeto = Projetos(codigoProjeto=1, descricao= "Viagem de férias")
objProjeto.tarefas.append(objTarefa1)
objProjeto.tarefas.append(objTarefa2)

for i in objProjeto.tarefas:
    print(i.numero , " ", i.descricao)
