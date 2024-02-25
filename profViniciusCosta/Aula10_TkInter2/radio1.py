import tkinter as tk
from tkinter import (ttk, )

janela = tk.Tk()
janela.title("Botão de Rádio")

# 'Responsividade' na Janela:
porcentual:float = 80/100
geometria:str = f"{int(janela.winfo_screenwidth()*porcentual)}x{int(janela.winfo_screenheight()*porcentual)}"
janela.geometry( geometria )
janela.resizable(False, False)


varRadio = tk.StringVar()
varRadio.set('0')
radio1 = tk.Radiobutton(janela, variable=varRadio, value='1', text="Masculino")
radio2 = tk.Radiobutton(janela, variable=varRadio, value='2', text="Feminino")
radio1.pack()
radio2.pack()


varPython = tk.StringVar(value=False)
varJs = tk.StringVar(value=0)
varHtml = tk.StringVar(value=False)

chkPython = tk.Checkbutton(janela, text="Python", variable=varJs)
chkJs = tk.Checkbutton(janela, text="Javascript", variable=varPython)
chkHtml = tk.Checkbutton(janela, text="HTML", variable=varHtml, command=lambda: print(varHtml.get() ) )
chkPython.pack()
chkJs.pack()
chkHtml.pack()


pb1 = ttk.Progressbar(janela, length=300, mode="indeterminate")
pb1.start(10) # ms
pb1.pack()







janela.mainloop()