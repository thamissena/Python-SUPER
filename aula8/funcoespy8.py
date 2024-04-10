products =[ ]

def add_product(prodName,prodQtd,prodValue):
    products.append({'produto':prodName,'quantidade':prodQtd, 'valor': prodValue, 'total' : prodQtd*prodValue})
    global totalProdutos
    totalProdutos = sum(produto['total'] for produto in products)
    print("\nProduto adicionada com sucesso!")
    print (f"{prodName}:\nQuantidade: {prodQtd}\nValor unitário: R$ {prodValue:.2f}\nValor total: R$ {prodQtd*prodValue:.2f}\nValor total de todos os produtos: R$ {totalProdutos:.2f}") 
    
    
def lits_products ( ):
   if not products: 
     print ("\nNenhuma produto registrado.")
   else: 
     print("\n LISTA DE COMPRAS:")  
     for idx, product in enumerate(products):
         print(f"{idx +1}. {product['produto']} - Quantidade: {product['quantidade']} - Valor unitário: R$ {product['valor']:.2f}, Valor total: R${product['total']:.2f}")
     totalProdutos = sum(produto['total'] for produto in products)
     print(f"\nValor total de todos os produtos:{totalProdutos:.2f}")

def renew_product(newProd):
    for product in products:
        if product['produto'] == newProd:
            new_name = input("Digite o novo nome do produto(deixe em branco para manter o mesmo): ").upper()
            new_qtd = input("Digite a nova quantidade(deixe em branco para manter o mesmo): ")
            new_value = input("Digite o novo valor unitário(deixe em branco para manter o mesmo): ")
            if new_name.strip( ):
                product['produto'] = new_name
            if new_qtd.strip( ):
                product['quantidade'] = float(new_qtd)
            if new_value.strip( ):
                product['valor'] = float(new_value)
            print("Produto atualizado com sucesso!")
        else:
          print ("\nProduto não encontrado.")
        if product['produto'] == newProd:
          product['total'] = product['valor']*product['quantidade']

def remove_product (escolhidoProd):
    for product in products:
      if product['produto'] == escolhidoProd :
         products.remove(product)
         print('\nProduto removido.')
      else:
         print ("\nProduto não encontrado.")