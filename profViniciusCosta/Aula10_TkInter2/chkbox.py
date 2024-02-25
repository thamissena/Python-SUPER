from tkinter import *

# Função para imprimir o valor da variável varC3 quando o botão é clicado
def valorVarC3():
    print(f"'{varC3.get()}' - True" if int(varC3.get()) else f"'{varC3.get()}' - False")

# Crie a janela principal
app = Tk()
app.geometry("600x400")
app.title("Exemplos de CheckButton usando posicionamento com GRID() - TkInter v.1.2")

# Crie as variáveis para os Checkbuttons
varC1 = StringVar()
varC2 = StringVar()
varC3 = StringVar()
varC1.set("1")
varC2.set("0")
varC3.set("1")

# Crie o Frame 1
frm1 = Frame(app, relief=RAISED, borderwidth=2)
frm1.grid()

# Crie um Checkbutton no Frame 1
Checkbutton(frm1, text="Dentro do Frame 1", variable=varC1).grid(column=0, row=0)
Checkbutton(frm1, text="Dentro do Frame 1").grid(column=0, row=3)

# Crie o Frame 2
frm2 = Frame(app, relief=RAISED, borderwidth=2)
frm2.grid()

# Crie um Checkbutton no Frame 2
Checkbutton(frm2, text="Dentro do Frame 2", variable=varC2).grid(column=0, row=0)

# Crie o Frame 3
frm3 = Frame(app, relief=RAISED, borderwidth=2)
frm3.grid()

# Crie Checkbuttons no Frame 3 com diferentes posições
Checkbutton(frm3, text="Dentro do Frame 3", variable=varC3).grid(column=0, row=0)
Checkbutton(frm3, text="Dentro do Frame 3", variable=varC3).grid(column=1, row=1)
Checkbutton(frm3, text="Dentro do Frame 3", variable=varC3).grid(column=2, row=2)

# Crie um Checkbutton no Frame 3 com uma função de callback
Checkbutton(frm3, text="Dentro do Frame 3", variable=varC3, command=valorVarC3).grid(column=3, row=3)

# Inicie o loop principal da interface gráfica
app.mainloop()