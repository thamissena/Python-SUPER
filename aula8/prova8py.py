from funcoespy8 import*
#Lista de compras:

print ("\n LISTA DE COMPRAS")
while True:
    print("\nMenu:")
    print("1. ADICIONAR produto")
    print("2. VISUALIZAR lista de produtos")
    print("3. ATUALIZAR produto")
    print("4. REMOVER produto")
    print("5. Fechar lista de compras")
    opcao = input ("\n Digite o número correspondente no que deseja realizar: ")
     
    if opcao=="1":
        print("\nAdicionar produto:")
        product_name = input("Insira o nome do produto: ").upper()
        product_qtd = float(input("Insira sua quatidade: "))
        produvt_value = float(input("Valor unitário do produto: "))

        add_product(product_name,product_qtd,produvt_value)

    elif opcao == "2":
       lits_products( )
    
    elif opcao == "3":
        lits_products()
        product_update =(input("\n Digite o nome do produto que deseja atualizar : ")).upper()
        renew_product(product_update)

    elif opcao=="4":
       lits_products( )
       product_del = input("\nDigite o nome do produto que deseja remover: ").upper()
       remove_product(product_del)

    elif opcao == "5":
       break 
    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida. ") 


