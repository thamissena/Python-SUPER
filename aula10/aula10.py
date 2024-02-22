from tkinter import *
from tkinter import ttk


root = tk()

root.geometry ("250X400")
root.title ("App de teste")

def iniciar_barra( ):
    button.configure (state= DISABLED)
    atualizar_barra(0)
    
def atualizar_barra(value):
    progress_bar["value"]= value

    if value < 100 and growing:
        value += 1
        root.after(20, atualizar_barra , value, growing)
    else:
        growing = False
    if value > 0 and not growing:
        value -=1
        root.after(20, atualizar_barra , value, growing)
    else:
        growing = True
        #button.configure(state=NORMAL)

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]

combobox = ttk.Combobox(root, values=dias_semana)
combobox.pack()

progresso = ttk.Progressbar (janela, length= 300, mode = "determinate")
barra_de_progresso.pack(pady=10)



button = (root, length= 300, mode=" ")

barra_de_progresso = ttk.Progressbar (janela, length= 300, mode = "determinate")
barra_de_progresso.pack(pady=10)

