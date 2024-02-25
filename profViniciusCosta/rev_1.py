preco = 1
total = 0
while preco>0:
    preco = float( input("Digite PREÇO: "))
    total += preco
print(f"Total a pagar R${total}")

exit()
for n in range(100):
    print(n)

x=0
while True:
    print("1 - Inclusão")
    print("2 - Alteração")
    print("3 - Exclusão")
    print("4 - SAIR")
    op= input(": ")
    match (op):
        case '1':
            print("Inclusão de Dados")
        case '2':
            print("Alteração de Dados")
        case '3':
            print("Exclusão de Dados")
        case '4':
            break

exit()
'''
    Palíndrome:
'''
palavra = input("Digite uma PALAVRA: ").strip().lower()

if palavra == palavra[::-1]:  
    print(f"A palavra {palavra} é um Palíndromo")
else:
    print(f"A palavra {palavra} NÃO é um Palíndromo")

exit()
"""
    Criar um App que o usuário informa (digita) um
    texto, e o mesmo é impresso invertido.
    ATENÇÃO: Sem usar slice (Fatiamento, [])
"""
texto = input("Informe um TEXTO: ").strip().upper()
# len() -> Length (Tamanho da String)
# Ana
# 012
for letra in range(len(texto)-1,-1,-1):
    print(texto[letra], end='')

exit()
print( "Infinity School"[::-1] )
print( "VINICIUS"[-1]) # S
print( "VINICIUS"[0]) # V
print( len("VINICIUS") ) # 8

valor=int( input("Digite um Inteiro: ") )
for numero in range(valor + 1):
    print(numero, end=' ')
exit()

lista = list( range(1,100, 2) )
print(lista)
exit()

lampadaEstaLigada = False
lampadaEstaLigada = not lampadaEstaLigada
nota = float( input("Informe a NOTA do Estudante: ") )
faltas = int( input("Informe a Quantidade de Faltas: ") )
if (nota>=7):
    if (faltas<10):
        print("Aprovado")

if (nota>=7) and (faltas<10):
    print("Aprovado")

# TkInter | SimpleGUI | Qt5


exit()

estadoCivil = input("Informe seu Estado Civil: ").strip().upper()
match (estadoCivil):
    case "SOLTEIRO":
        print("Estado Civil: Solteiro")
    case "CASADO":
        print("Estado Civil: Casado")
    case "VIUVO":
        print("Estado Civil: Viuvo")
    case _:
        print("Opção inválida!")

exit()

print(1==True)

exit()

if True:
    print("Sempre Verdadeiro")

if 1:
    print("Sempre Verdadeiro")


