"""
#dicionario
usuario = {'nome': 'pedro','idade':12}
for chaves,valores in usuario.items():
    print(f"{chaves}: {valores}") 
    
dicionario = dict()
# Receber a chave e o valor do usuário
chave1 = input("Digite a chave: ")
valor1 = input("Digite o valor: ")
# Adicionar ou atualizar o item no dicionário
dicionario = {chave1:valor1}
#dicionario[chave] = valor
# Exibir o dicionário atualizado
print("Dicionário atualizado:", dicionario)

numeros = {elemento:f'Valor{elemento}' for elemento in range(6)}
print (numeros) 
"""

#Crie um programa que simule um sistema de votação. O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.
votos = { }

print("Bem-vindo ao sistema de votação!")

# Loop principal
while True:
    print("\nOpções de votação:")
    print("1. Opção A")
    print("2. Opção B")
    print("3. Opção C")
    print("0. Encerrar a votação e exibir resultados")

    # Receber o voto do eleitor
    voto = input("Digite o número da opção desejada ou 0 para encerrar: ")

    # Verificar se o usuário deseja encerrar a votação
    if voto == '0':
        print("\nEncerrando a votação...")
        break

    # Verificar se o voto é válido
    if voto not in ['1', '2', '3']:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        continue

    # Atualizar contagem de votos
    if voto in votos:
        votos[voto] += 1
    else:
        votos[voto] = 1

# Exibir os resultados finais
print("\nResultados da votação:")
for opcao, votos_recebidos in votos.items():
    print(f"Opção {opcao}: {votos_recebidos} votos.")

print("Votação encerrada.")

# Inicializar dicionário para mapear opções aos votos
votos = {'1': 'Opção A', '2': 'Opção B', '3': 'Opção C'}

print("Bem-vindo ao sistema de votação!")

# Inicializar dicionário para armazenar os votos recebidos
resultados = {opcao: 0 for opcao in votos.values()}

# Loop principal
while True:
    print("\nOpções de votação:")
    print("1. Opção A")
    print("2. Opção B")
    print("3. Opção C")
    print("0. Encerrar a votação e exibir resultados")

    # Receber o voto do eleitor
    voto = input("Digite o número da opção desejada ou 0 para encerrar: ")

    # Verificar se o usuário deseja encerrar a votação
    if voto == '0':
        print("\nEncerrando a votação...")
        break

    # Verificar se o voto é válido
    if voto not in votos:
        print("Opção inválida! Por favor, escolha uma opção válida.")
        continue

    # Atualizar contagem de votos
    resultados[votos[voto]] += 1

# Exibir os resultados finais