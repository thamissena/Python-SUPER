import tkinter as tk

root = tk.Tk()

varLogin = tk.StringVar()
varSenha = tk.StringVar()

lblTitulo = tk.Label(root, text="Login")
lblTitulo.grid(row=0, column=0, columnspan=2)

lblLogin = tk.Label(root, text="Login: ")
lblLogin.grid(row=1, column=0)

txtLogin = tk.Entry (root)
txtLogin.grid(row=1,column=1)

lblSenha = tk.Label(root, text="Senha: ")
lblSenha.grid(row=2, column=0)

txtSenha = tk.Entry (root)
txtSenha.grid(row=2,column=1)

btnLogin = tk.Button(root, text="Login")
btnLogin.grid(row=3, column=1,  sticky="W")

root.mainloop()