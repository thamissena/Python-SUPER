from tkinter import *


root = Tk()
root.geometry("400x540")

#State
varNumberon = StringVar ()
varNumbertw = StringVar ()
varResultado = IntVar ()

def btnSomarOnClick():
    print(varNumberon.get())
    print(varNumbertw.get())
    
    varResultado.set(int(varNumberon.get())+int(varNumbertw.get()))
    
lblTitulo = Label(root, text="A soma de doi números:", font=("Arial", 12) )
lblTitulo.pack()

txtNumbero = Entry(root, textvariable= varNumberon)
txtNumbero.pack()

txtNumbert = Entry(root, textvariable= varNumbertw)
txtNumbert.pack()


btnSoma = Button(root, text="Calcular", command= btnSomarOnClick)
btnSoma.pack()

lblResultado = Label(root, textvariable= varResultado)
lblResultado.pack()

root.mainloop()
