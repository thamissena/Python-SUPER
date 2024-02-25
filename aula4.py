
def calculadora(a:float,b:float) -> float:
     while True:
        opcao = input ('Digite 1 para somar, 2 para subtrair, 3 para multiplicar, 4 para dividir e 0 para sair do programa:  ')
        if opcao == '0': 
            print('\nPrograma encerrado.')
            break
        if opcao== '1':
            print(a+b)

        if opcao == '2':
            print(a-b)

        if opcao == '3':
            print(a*b)
        else:
            print(a/b)

num1 = float(input("Insira um número:"))
num2 = float(input("Insira um número:"))
print (calculadora(num1,num2))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == '1':
                print("Resultado:", soma(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtracao(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicacao(num1, num2))
            elif escolha == '4':
                print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            print("Calculadora encerrada.")
            break
        else:
            print("Escolha inválida. Tente novamente.")


exit()

def saudacao(nome):
    print(f"olá!{nome}")

saudacao('Ana')

def saudacao(nome):
    return f"olá!{nome}"

print(saudacao('Ana'))
nome = input ("Digite seu nome: ")

def soma(a:int, b:int) -> int:
    #A soma de dois números interiros
    return a+b
num1 = int(input("Insira um número:"))
num2 = int(input("Insira um número:"))
print(soma(num1,num2))

def horario(hora):
    if 00 <= hora and hora <=12:
        print ("Bom dia!")
    elif 12 < hora and hora <=18:
        print("Boa tarde!")
    else:
        print("Boa noite!")
        
hora = int(input("Digite que horas são: "))
horario(hora)


