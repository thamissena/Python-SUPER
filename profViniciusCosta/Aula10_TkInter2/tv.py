import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

dicDados = {
    1: ["João Silva", "joao.silva@gmail.com", "(71) 999.888.777"],
    2: ["Maria Santos", "maria.santos@gmail.com", "(75) 999.666.555"],
    3: ["Pedro Almeida", "pedro.almeida@gmail.com", "(71) 999.888.111"],
    4: ["Ana Costa", "ana.costa@gmail.com", "(71) 999.888.222"],
    5: ["Lucas Oliveira", "lucas.oliveira@gmail.com", "(71) 999.888.333"],
    6: ["Fernanda Lima", "fernanda.lima@gmail.com", "(71) 999.888.444"],
}

janela = tk.Tk()

# Criando a TreeView:
tabela = ttk.Treeview(janela)

# Definição das colunas:
tabela["columns"]=("nome", "email", "telefone")

# Formatação das colunas:
tabela.column("#0", width=100, minwidth=100, anchor=tk.CENTER)
tabela.column("nome", width=150, minwidth=150, anchor=tk.CENTER)
tabela.column("email", width=150, minwidth=150, anchor=tk.CENTER)
tabela.column("telefone", width=150, minwidth=150, anchor=tk.CENTER)

# Definição do Cabeçalho da Tabela:
tabela.heading("#0", text='' )
tabela.heading("nome", text="N O M E",command=lambda: messagebox.showinfo('',"Título da coluna NOME!") )
tabela.heading("email", text="E M A I L" )
tabela.heading("telefone", text="T E L E F O N E" )

# Inserindo os dados:
for chave, valor in dicDados.items():
    tabela.insert('', tk.END, text=str(chave), values=tuple(valor) )

# Função ativada pelo Evento de Seleçãom dos dados:
def funcItemSelecionado(e):
    selecao = tabela.focus()
    messagebox.showinfo('', tabela.item(selecao))

# Gerando o manipulador de Eventos de Seleção da TreeView:
tabela.bind("<ButtonRelease-1>", funcItemSelecionado)

tabela.pack()


janela.mainloop()