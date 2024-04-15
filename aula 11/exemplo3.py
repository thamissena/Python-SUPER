class Pessoa:
    total_de_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_de_pessoas += 1

    
p1 = Pessoa("Maria")
p2 = Pessoa("João")
print(p1.total_de_pessoas)
print(p2.total_de_pessoas)
print(Pessoa.total_de_pessoas)

