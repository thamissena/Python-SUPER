def calcular_media (notas):
    return sum (notas)/len (notas)


def verificar_situacao (media):
    if media < 7 : 
        print ("Reprovado.")
    elif media == 10 :
        print("Parabéns, sua média é 10.")
    else:
        print("Aprovado!")


notas = [ ]

while True:
    nota = input ("Digite uma nota ou 'sair' para encerra.\n ")
    if nota.lower() == 'sair':
         break
    else:
        notaNum = float(nota)
        notas.append(notaNum)

media = calcular_media (notas)
print (f"Média : {media:.2f}")
print (verificar_situacao(media))
