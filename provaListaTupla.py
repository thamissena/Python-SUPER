valores = []
quantidade = 0
while quantidade < 10:
    quantidade+=1
    valor = int(input("Insira um valor:"))
    valores.append(valor)
print ("Lista dos valores digitados:", valores)

valorpar = []
valorimpar = []
for valor in valores: 
    if valor%2 == 0: 
     valorpar.append(valor)
     somapar=sum (valorpar)   
    else:
        valorimpar.append(valor)
        somaimpar= sum(valorimpar)

print("Números pares:", valorpar)
print("Números ípares:", tuple(valorimpar))
print("Quantidade de número pares:",len(valorpar))
print("Quantidade de número ímpares:",len(valorimpar))
print(f"A soma dos números pares é igual a {somapar} e a soma dos números ímpares é igual a {somaimpar}.")