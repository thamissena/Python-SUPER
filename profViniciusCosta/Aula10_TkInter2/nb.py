import tkinter as tk
import tkinter.ttk as ttk

# Função para tratar a seleção de guias
def selecionar(event):
    current_tab_index = notebook.index(notebook.select())
    current_tab_text = notebook.tab(current_tab_index, "text")
    print(f"Guia selecionada: {current_tab_text}")

# Crie a janela principal
janela = tk.Tk()
janela.geometry("400x400")

# Crie um Notebook para abas
notebook = ttk.Notebook(janela, width=350, height=200)

# Crie a primeira guia (aba)
guia1 = ttk.Frame(notebook, relief="raised", borderwidth=3)
botao1 = ttk.Button(guia1, text="Botão 1").pack()
botao2 = ttk.Button(guia1, text="Botão 2").pack()
botao3 = ttk.Button(guia1, text="Botão 3").pack()

# Crie a segunda guia (aba)
guia2 = ttk.Frame(notebook, relief="sunken", borderwidth=3)
txt = ttk.Entry(guia2).pack()

# Adicione as guias ao Notebook
notebook.add(guia1, text="Guia 1")
notebook.add(guia2, text="Guia 2")

# Coloque o Notebook na janela principal
notebook.pack()

# Vincule o evento de seleção de guia ao Notebook
notebook.bind("<<NotebookTabChanged>>", selecionar)

# Inicie o loop principal da interface gráfica
janela.mainloop()