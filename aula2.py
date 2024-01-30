"""lista1 = [1,2,3,4,5]
print (lista1)

lista2 = ['a','e','i','o','u']
print(lista2)"""

# Defina uma lista com 5 itens que tenha, pelo menos, 3 classes diferentes. Utilize o print() para exibir o terceiro elemento dessa lista

"""lista3 = [2, "Ana", 3.45, ['a','e','i','o','u'],'João']
print(lista3[2])
print(lista1[-1]) #o número é 5, o ultimo numero da lista. """

#ATIVIDADE PRÁTICA 4 - TUPPLA: Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

"""palestra = (('Paulo', 'IA na Engenharia', 'UFBA'),
            ('Roberta', 'Melhores Softwares do mercado.', 'UNIFACS'),
            ('Beatriz','Novidades de 2024','IFBA'))
#print('Terceira palestra:', palestra[2])
#terceiro_palestrante = palestra[2]
#nome, tema, instituicao = terceiro_palestrante
nome, tema, instituicao = palestra [2] # isso seria desempacotar um tupla

print("Informações do Terceiro Palestrante:")
print("Nome:", nome)
print("Tema da Palestra:", tema)
print("Instituição: .\n", instituicao )"""

"""DESAFIO PRÁTICO
Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas representando os resultados das equipes em diferentes modalidades. Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição.

1.Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente.
3.Crie uma nova lista chamada classificacao que contém tuplas, onde cada tupla contém o nome da equipe e sua média de pontuações.
4.Exiba na tela a classificação final das equipes, mostrando o nome da equipe e sua média, da equipe com a pontuação mais alta para a mais baixa."""

#tem uma lista de tuplas - Cada tupla contém o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da competição.
equipes = [
    ('equipe1', [3,4,6]),
    ('equipe2', [5,6,7]),
    ('equipe3', [7,2,5])
]
medias = []
for equipe, pontuacao in equipes:
    medias_pontuacao =round(sum (pontuacao)/len (pontuacao), 2)
    medias.append(medias_pontuacao)
#Ordene a lista medias em ordem decrescente.
medias_ordenadas = sorted(medias, reverse=True)
print(medias_ordenadas)

classificacao = [(equipe, media) for media, (equipe, _) in zip( medias_ordenadas, equipes)]
print(classificacao)


posicao1, posicao2, posicao3 = classificacao
#primeiro, media1 = posicao1
primeiro, media1 = classificacao [0]
segundo, media2 = classificacao [1]
terceiro, media3 = classificacao[2]
print(f'Primeira lugar { primeiro}, com media {media1} ')
print('Segunda equipe: ', posicao2)
print('Terceira equipe: ', posicao3)
"""lugar = 0
for equipe, media in classificacao:
    lugar += 1
    print(f'{equipe} - {media} - {lugar}º lugar')"""

"""Métodos para manipulação de lista:
    -Adição de itens : .append() - Adicionar um elemento ao final da lista.
    -Adição de itens: .insert() - Adicionar um elemento na posição informada.
    -Remoção de itens: .remove() - Remover um elemento de uma lista através de seu índice.
    -Remoção de itens: .pop() - Remover um elemento de uma lista através de seu valor."""








