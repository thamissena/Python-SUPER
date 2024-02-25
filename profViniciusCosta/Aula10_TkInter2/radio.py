from tkinter import (Tk, Button, Entry, Label, StringVar, Radiobutton, BooleanVar)

# instanciar um objeto 'Master Window'
janela = Tk()
janela.title("Estoque v1.0")    # Título da Janela
porc = 60/100   # Porcentual tamanho da Tela
geometria = f"{ janela.winfo_screenwidth() }x{ int( janela.winfo_screenheight() * porc ) }"
janela.geometry(geometria)
janela.resizable("False", "False")  # Redimensionavel(largura, altura)

tituloCliente = Label(janela, text="Digite o NOME do Cliente: ")
tituloCliente.place(x=10, y=10)

varNome = StringVar()
caixaCliente = Entry(janela, width=200, textvariable=varNome)
caixaCliente.place(x=10, y=30)

txtGenero = StringVar()
txtGenero.set('2')
genero1 = Radiobutton(janela, text="Masculino", variable=txtGenero , value='1').place(x=10, y=60)
genero2 = Radiobutton(janela, text="Feminino", variable=txtGenero, value='2').place(x=100, y=60)


import tkinter.messagebox as msgbox

def salvar():
    r = msgbox.askyesnocancel("SALVAR", "Confirma" + varNome.get() )
    if r:
        print("Salvando...", txtGenero.get())
    elif r == None:
        print("Ação Cancelada!")
    else:
        print("Não será salvo!")


btnSalvar = Button(janela, text="Salvar", command=salvar)
btnSalvar.place(x=10, y=100)












janela.mainloop()