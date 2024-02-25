lista=['a', 'b', 'c', 'd', 'b', 'e', 'b']
lista2 = set(lista)
print(lista)
print(lista2)
lista2.discard('b')
print(lista2)
lista2.discard('z')


exit()
a = set({1,2,3,4,5})
b = set({9,8,7,6,5})
c = set({'S', 'A', 'Z'})
print("Interseção: ", a.intersection(b) )
print("União: ", a.union(b) )

exit()

print( list(range(10) ) )
dic6 = ["Hum", "Dois"]
print( dict.fromkeys( dic6, 0) )

dic7 = {}.fromkeys(range(1,41), True)
dic7[33] = False
print(dic7)
print( dic7.items() )
input('...')
print( list(dic7.values() ) )
input('...')
print( list(dic7.keys() ) )
exit()
# Criando um Dicionário com o
dic4 = { 
    1: "Vinicius",
    2: "Ana",
    1: "Maria",
}
print(dic4)
print( len(dic4) )  # 2

# Copia do Dicionário:
dic5 = dic4.copy()
dic5[1] = "João"
print("Dicionário 4: ", dic4)
print("Dicionário 5: ", dic5)

# Exclusão de Dados:
del dic4[2]
print(dic4)
print("infinity".title())
backup = dic4.pop(1)
print(backup)   # Maria

# Inserir/Alterar Valor:
dic4[3] = "Juliana"
print(dic4)

dic4.clear()
print(dic4)

exit()

# 'Construtor' da Classe 'Dict':
dic3 = dict(
    aaa1 = "Vinicius",
    aaa2 = "Ana Clara",
    aaa3 = "Maria Julia",
)
print(dic3)
chave = input("Digita Chave: ").strip()
valor = input("Digite o Valor: ").strip()

# Inserir dados no Dicionário:
dic3[chave] = valor

print(dic3)



exit()


dic2 = {n:n**2 for n in range(11)}
print(dic2)

# Dicionário Vazio:
dic1 = {}
dic = dict()

# Lista Vazia:
lista = []
lista2 = list()
tupla1 = tuple()
tupla2 = (None,)

exit()
dicionario = {
    "Modulo":"Python",
    "Instituicao":"infinity School",
}

print(dicionario)