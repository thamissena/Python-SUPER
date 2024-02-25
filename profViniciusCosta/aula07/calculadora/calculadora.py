from operacoes import *

menu = {
    1: ["Somar", "somar("],
    2: ["Subtrair", "subtrair("],
    3: ["Multiplicar", "multiplicar("],
    4: ["Dividir", "dividir("],
    5: ["Sair", "exit()"],
}

while True:
    for item in menu:
        print(f"{item} - {menu[item][0]}")
    opcao = int( input(': ') )
    valores = ''
    while True:
        valores += input("Digite o valor:")
        valores += ','
        resposta = input("S/N?")
        if resposta=='N': break
    valores = valores + ')'
    expressao = menu[opcao][1] + valores
    print( eval( expressao )  )
