from tkinter import*

def calcular():
    a=int(ECantidad.get())
    resultado=a*4/1000
    EResultado.delete(0,END)
    EResultado.insert(0,resultado)

gui=Tk()
gui.geometry("340x230")

LCantidad=Label(gui,text="Ingresar Cantidad de Dinero:")
LResultado=Label(gui,text="Resultado")
ECantidad=Entry(gui,width=10)
EResultado=Entry(gui,width=20)
BCalculo=Button(gui,text="4X1000",command=calcular)

LCantidad.pack()
ECantidad.pack()
BCalculo.pack()
LResultado.pack()
EResultado.pack()
gui.mainloop()
