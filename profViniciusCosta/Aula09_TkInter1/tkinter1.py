import tkinter as tk
from tkinter import (messagebox, font)
def exibirMsg():
    messagebox.showinfo(title="Mostrar Produto", message="Produto: " + str(varNome.get() ) )
    messagebox.showerror(title="Mostrar Produto", message="Produto: " + varNome.get() )
    messagebox.showwarning(title="Mostrar Produto", message="Produto: " + varNome.get() )
# Instanciando um objeto da Classe Tk:
janela = tk.Tk()    # Construtor
janela.geometry("600x600") # String: Largura x Altura da Janela em Pixel
janela.title("Controle de Estoque - v.1.02")
# Rótulo do Nome do Produto:
lblNome = tk.Label(janela, text="Digite o Nome do PRODUTO: ", bg="red", fg="white", 
                   font=("Arial", 12, 'bold') )
lblNome.place(x=10 , y=10)
# Caixa de Texto do Nome do Produto:
varNome = tk.DoubleVar()  #tk.IntVar(), tk.DoubleVar(), tk.BooleanVar()
txtNome = tk.Entry(janela, textvariable=varNome, width=50, font=("Arial", 22) )
txtNome.place(x=10, y=40)

frmBotao = tk.Frame(janela, relief=tk.GROOVE, borderwidth=3, width=300, height=150)
frmBotao.place(x=30, y=250)

# Botão:
btnExibir = tk.Button(frmBotao, text="Exibir", command=exibirMsg )
btnExibir.place(x=32, y=25)

# CheckButton:
lpJava = tk.Checkbutton(janela, text="Linguagem Java").place(x=10, y=450)
lpPython = tk.Checkbutton(janela, text="Linguagem Python").place(x=10, y=480)
lpJS = tk.Checkbutton(janela, text="Linguagem Javascript").place(x=10, y=500)

# RadioButton:
rdMasculino = tk.Radiobutton(janela, text="Masculino").place(x=10, y=530)
rdFeminino = tk.Radiobutton(janela, text="Masculino").place(x=10, y=560)









janela.mainloop()