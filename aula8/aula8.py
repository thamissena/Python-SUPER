#Função agregadoras:
#ATIVIDADE 5:
vendas= {
    'produto1':200,
    'produto2':150,
    'produto3':200,
    'produto4':100,
    'produto5':170
}
mais_vendido = max(vendas.values())
print(mais_vendido)
produtos_mais_vendidos = []
for pronduto, vendas in vendas.items():
   if vendas== mais_vendido: 
      produtos_mais_vendidos.append(pronduto)
print(produtos_mais_vendidos)

#ATIVIDADE 6:
def contar_impares_e_pares(lista):
    impares = list(filter(lambda x: x % 2 != 0, lista))
    pares = list(filter(lambda x: x % 2 == 0, lista))
    num_impares = len(impares)
    num_pares = len(pares)
    return num_impares, num_pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_impares, num_pares = contar_impares_e_pares(numeros)
print("Número de ímpares:", num_impares)
print("Número de pares:", num_pares)

#ATIVIDADE 7:
def calcular_media_trimestral(vendas_trimestrais):
    medias = []
    for trimestre in vendas_trimestrais:
        soma_trimestral = sum(trimestre)
        media_trimestral = soma_trimestral / 3  # Número de meses em um trimestre
        medias.append(media_trimestral)
    return medias
# Exemplo de vendas trimestrais
vendas_trimestrais = [
    [10000, 12000, 15000],  # Janeiro a março
    [13000, 14000, 16000],  # Abril a junho
    [11000, 12500, 15500],  # Julho a setembro
    [13500, 14500, 16500]   # Outubro a dezembro
]

medias_trimestrais = calcular_media_trimestral(vendas_trimestrais)
for i, media in enumerate(medias_trimestrais, start=1):
    print(f"Média de vendas no trimestre {i}: {media}")

def mais_soma_trimestre(vendas_trimestrais):
    maior_soma = []
    for trimestre in vendas_trimestrais:
        soma_trimestral = sum(trimestre)
        maior_soma.append(soma_trimestral)
        maior_trimestre = max (maior_soma)
        return maior_trimestre
def menor_soma_trimestre(vendas_trimestrais):
    menor_soma = []
    for trimestre in vendas_trimestrais:
        soma_trimestral = sum(trimestre)
        menor_soma.append(soma_trimestral)
        menor_trimestre = min(menor_soma)
        return menor_trimestre
def calcular_total_anual(vendas_trimestrais):
    total_anual = sum(sum(trimestre) for trimestre in vendas_trimestrais)
    return total_anual

print(f'Maior soma = {mais_soma_trimestre(vendas_trimestrais)}, menor soma= {menor_soma_trimestre(vendas_trimestrais)}, Vendas anual = { calcular_total_anual(vendas_trimestrais)}')

#------------------------------------------------
#ATIVIDADE 1 :
lista1 = [ 1,2,3,4,4,5,6,7,8,9]
listapar = [ ]
for valor in lista1: 
    if valor%2 == 0: 
     listapar.append(valor)
print(listapar)

lista2 = [3,10,5,6,7,8,9,9,0]
lista_pares = [num for num in lista2 if num % 2 == 0]
print(lista_pares)

#ATIVIDADE 2:

produtos = {}

# Função para adicionar um novo produto
def adicionar_produto(nome, preco, quantidade):
    produtos [nome] = {'preco': preco, 'quantidade': quantidade}
    print(f"Produto '{nome}' adicionado com sucesso.")
adicionar_produto('camisa',20,3)    
print(produtos)
# Função para remover um produto
def remover_produto(nome):
    if nome in produtos:
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado.")
# Função para atualizar informações de um produto
def atualizar_produto(nome, preco_novo=None, quantidade_nova=None): #permite que eu atualize sem a obrigacao de definer os dois argumentos, None significa quem nao tem valor
    if nome in produtos:
        if preco_novo is not None:
            produtos[nome]['preco'] = preco_novo
        if quantidade_nova is not None:
            produtos[nome]['quantidade'] = quantidade_nova
        print(f"Informações do produto '{nome}' atualizadas com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado.")
atualizar_produto('camisa', preco_novo=25.99)
print(produtos)

#ATIVIDADE 3 
cores = {'azul', 'vermelho','amarelo'}

def coresquatro (cores):
    for cor in cores:
        return {cor for cor in cores if len(cor) > 4}
print(coresquatro(cores))

#ATIVIDADE 4:
#string é um palíndromo (lê-se igual de trás para frente).

lista3 = ['azul', 'arara','verde']
def palindromo (lista3):
  listanova = []
  for palavra in lista3:
      if  palavra == ''.join(reversed(palavra)):
       listanova.append(palavra)
       print(listanova)
palindromo(lista3)
