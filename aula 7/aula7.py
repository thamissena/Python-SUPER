#BIBLIOTECAS:
#Atividade 3:
import math
#Área do quadro:
x=3
quadradro  = math.pow(x,2)
print(quadradro)
#área do retângulo:
comprimento = 3 
largura = 6 
retangulo = comprimento * largura 
#área do circulo:
r=7
circulo = math.pi * math.pow(r,2)
import random
#ATIVIDADE 4 - JOGO DE ADIVINHA 

def jogo_de_adivinhacao():
 lista = list(range(1,11))
 numeroSorteado = random.choice(lista)
 tentativa = 0 
 while True:
    numeroEscolhido = int(input("Escolha um número de 1 a 10: "))
    tentativa += 1

    if numeroEscolhido not in lista:
      print("O número escolhido não está dentro do intervalo requerido.Tente novamente.")
    elif numeroEscolhido != numeroSorteado:
      if numeroEscolhido < numeroSorteado:
        print("O número sorteado é menor que o escolhido.Tente novamete.")
      else:
        print("O número sorteado é maior que o escolhido.Tente novamete.")
    else:
       print("Você acertou o número escolhido.")
       break
 jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
 if jogar_novamente == "sim":
        jogo_de_adivinhacao()
 else:
        print("Obrigado por jogar!")

jogo_de_adivinhacao() 



exit()
#----------------------------
import aula7_util
#ATIVIDADE PRÁTICA 2 :Crie um módulo chamado manipulacao_strings que contenha funções para realizar operações com strings, como inverter uma string, contar o número de palavras em uma string e verificar se uma string é um palíndromo (lê-se igual de trás para frente). Crie um programa principal que importe o módulo e use essas funções com strings fornecidas pelo usuário.

string = input("Imforme a frase ou palavra: ")
aula7_util.inverter(string)
aula7_util.contar(string)
aula7_util.palindromo(string)

#-------------------------
exit()
aula7_util.data_to_mysql('25/01/2023 20:20:00')