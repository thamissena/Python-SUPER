"""util.py
'yyyy-mm-dd hh:ii:ss'
'dd/mm/yyyy hh:ii:ss'
def data_to_mysql(data: str):
    pass
def mysql_to_data(data: str):"""

def data_to_mysql (data: str):
    print (data)
    data_formatada = data.split(" ") #transforma em um array, com dois elementos.
    print (data_formatada)
    data_formatada = data_formatada[0].split("/")
    print (data_formatada)
    print (f"{data_formatada[2]}-{data_formatada[1]}-{data_formatada[0]}")

#MANIPULAÇÃO DE STRINGS:
#inverter uma string:
def inverter (palavra):
  palavra_invertida = ''.join(reversed(palavra))
  print(palavra_invertida)

#contar o número de palavras em uma string 
def contar (palavra):
   palavras = palavra.split(" ")
   numero_palavras = len(palavras)
   print("Número de palavras: ", numero_palavras)
 
#verificar se uma string é um palíndromo (lê-se igual de trás para frente)
def palindromo (palavra):
 palavra_invertida = ''.join(reversed(palavra))
 if palavra == palavra_invertida : 
    print ("Essa string é um palíndromo.")
 else:
    print ("Essa string não é um palíndromo.")
    