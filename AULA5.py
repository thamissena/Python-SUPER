#https://gabriel-schade-cardoso.gitbook.io/python-aprendendo-a-programar/chapter12

#ATIVIDADE PRÁTICA 1 :Crie um programa que solicita ao usuário que insira três notas e, em seguida, calcule a média dessas notas usando uma função.
# A função deve receber as três notas como argumentos e retornar a média. Por fim, o
#programa deve imprimir a média calculada.

def media (a, b, c):
    resultado = (a+b+c)/3
    return resultado
# return (a+b+c)/3

nota1 = int(input ("Insira a primeira nota: "))
nota2 = int(input ("Insira a seegunda nota: "))
nota3 = int(input ("Insira a terceira nota: "))

print (media(a=nota1, b=nota2, c = nota3))
#print (media(nota1, nota2, nota3))
  

  #ATIVIDADE PRÁTICA 2 :Crie um programa que define uma função calcular_area_retangulo que recebe dois argumentos, comprimento e largura de um retângulo, e retorna a
#área desse retângulo. Em seguida, o programa deve solicitar ao usuário que insira o comprimento e a largura e imprimir a área calculada.

#exemplo arg

import math
def media(*args):
    soma = 0
    for nota in args:
        if not math.isnan (nota):
            soma = soma + nota
    return (soma)/len(args)


#ATIVIDADE PRÁTICA 3 : Crie uma função chamada concatenar_strings que aceita um número variável de strings como argumentos
#posicionais (usando *args). A função deve concatenar todas as strings em uma única string e retorná-la.