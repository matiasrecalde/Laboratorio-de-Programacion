import tkinter
from tkinter import ttk
ventana = tkinter.Tk()
ventana.resizable(height=0,width=0)
ventana.geometry("700x500")
boton_eliminar= tkinter.Button(ventana,text="eliminar",bg="green")
boton_crear= tkinter.Button(ventana,text="crear",bg="red")
boton_completar= tkinter.Button(ventana,text="completar",bg="blue")
cajadetexto= tkinter.Entry(ventana)
treeview = ttk.Treeview(columns=("descri", "compl"))
treeview.heading("#0", text="nombre")
treeview.heading("descri", text="fecha de creacion")
treeview.heading("descri", text="realizado")
treeview.insert(
    "",
     tkinter.END,
     text="comprar milanesa",
     values=("10/9/23", False))
treeview.pack()
cajadetexto.pack()
boton_crear.pack()
boton_completar.pack()
boton_eliminar.pack()
ventana.mainloop()