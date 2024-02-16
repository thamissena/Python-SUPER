from tkinter import *


root = Tk()
root.geometry("400x540")

#State
varNome = StringVar ()

def btnLoginOnClick():
    varNome.set("")
    
lblTitulo = Label(root, text="Olá Mundo", font=("Arial", 12) )
lblTitulo.pack()

txtNome = Entry(root, textvariable= varNome)
txtNome.pack()

#lblNome = Label(root, textvariable=varNome)
#lblNome.pack()

btnLogin = Button(root, text="Login", command= btnLoginOnClick)
btnLogin.pack()

root.mainloop()
