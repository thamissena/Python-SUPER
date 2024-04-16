from tkinter import*

root = Tk()
root.geometry("400x540")
root.title("Conversor de Centímetros para Metros")


varNumberon = StringVar ()
varResultado = IntVar ()

def btnConverterOnClick():
    print(varNumberon.get())
    
    varResultado.set(int(varNumberon.get())/100) 
    
lblTitulo = Label(root, text="Conversão de centímetos para metros: ", font=("Arial", 14) )
lblTitulo.grid(row=0, column=0, columnspan=2, pady=10)


txtNumbero = Entry(root, textvariable= varNumberon )
txtNumbero.grid(row=2, column=1, padx=10)




btnConverte = Button(root, text="Converter", command= btnConverterOnClick)
btnConverte.grid(row=4, column=1, columnspan=2, pady=10)


lblResultado = Label(root, textvariable = varResultado)
lblResultado.grid(row=6, column=1, columnspan=2)


root.mainloop()
