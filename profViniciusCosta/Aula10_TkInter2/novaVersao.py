import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("Botão de Rádio")

# Função para atualizar o rótulo de progresso
def atualizarPBar():
    return f"Progresso: {barra2['value']}%"

# Função para atualizar o progresso da segunda barra de progresso
def progresso():
    if barra2["value"] < 100:
        barra2["value"] += 5
        rotulo["text"] = atualizarPBar()
        janela.after(250, progresso)  # Atualize o progresso a cada 250 milissegundos
    else:
        showinfo(message="Tarefa completada!")

# Função p/ parar a segunda barra de progresso
def parar():
    barra2.stop()
    rotulo["text"] = atualizarPBar()

# Crie a primeira barra de progresso (indeterminada)
barra1 = ttk.Progressbar(janela, orient="horizontal", mode="indeterminate", length=280)
barra1.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# Botão para iniciar a primeira barra de progresso
btnIniciar1 = ttk.Button(janela, text="Iniciar 1", command=barra1.start)
btnIniciar1.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# Botão para parar a primeira barra de progresso
btnParar = ttk.Button(janela, text="Parar", command=barra1.stop)
btnParar.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

# Crie a segunda barra de progresso (determinada)
barra2 = ttk.Progressbar(janela, orient="horizontal", mode="determinate", length=280, value=0)
barra2.grid(column=0, row=4, columnspan=2, padx=10, pady=20)

# Rótulo para exibir o progresso atual
rotulo = ttk.Label(janela, text=atualizarPBar())
rotulo.grid(column=0, row=5, columnspan=2)

# Botão para iniciar a segunda barra de progresso
iniciar2 = ttk.Button(janela, text="Iniciar 2", command=progresso)
iniciar2.grid(column=0, row=6, padx=10, pady=10, sticky=tk.E)

# Botão para reiniciar a segunda barra de progresso
btnParar2 = ttk.Button(janela, text="Parar/Reiniciar", command=parar)
btnParar2.grid(column=1, row=6, padx=10, pady=10, sticky=tk.W)






janela.mainloop()