#Stes
set1 = set(['infinity','school', '202'])
print(set1)

#Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele:"maçã","banana","uva","laranja" e "morango". Em seguida, imprima o conjunto.
frutas = set()
frutas.add('banana')
frutas.add('maçã')
frutas.add ('uva')
frutas.update(['laranaja','morango'])
print(frutas)
#Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.
print('banana' in frutas)
#Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele:"morango","cereja" e "framboesa ". Em seguida, imprima o conjunto.
frutas_vermelha = {'morango','cereja','framboesa'}
frutas.update(frutas_vermelha) #print(frutas.union(frutas_vermelha))
print(frutas)
#Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.
print(frutas_vermelha.discard('cereja'))
#intersection dos conjuntos 
print (frutas.intersection(frutas_vermelha))
#Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.
def calcular_uniao(lista1, lista2):
    # Converter as listas em conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    
    # Calcular a união dos conjuntos
    uniao = conjunto1.union(conjunto2)
    
    return uniao

# Função para entrada das listas
def entrada_listas():
    lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
    lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()
    return lista1, lista2

# Função principal
def main():
    lista1, lista2 = entrada_listas()
    uniao = calcular_uniao(lista1, lista2)
    print("A união dos elementos únicos das listas é:", uniao)

if __name__ == "__main__":

    main()
# Receber entrada das listas
lista1 = input("Digite os elementos da primeira lista separados por espaço: ").split()
lista2 = input("Digite os elementos da segunda lista separados por espaço: ").split()
# Calcular a união dos elementos únicos usando conjuntos
uniao = set(lista1).union(set(lista2))
# Exibir o resultado
print("A união dos elementos únicos das listas é:", uniao)

