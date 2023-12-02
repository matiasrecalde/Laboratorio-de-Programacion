# Estas son las importaciones
from tkinter import ttk
import tkinter
from tkinter import messagebox
from datetime import datetime

# Esta es la ventana de tkinter
ventana = tkinter.Tk()
ventana.resizable(height=0,width=0)
#Tamaño de ventana
ventana.geometry("700x300")


def confirmar_eliminar():
   seleccion = treeview.selection()
   if seleccion:
       confirmar = messagebox.askokcancel("Confirmar", "¿Estás seguro de eliminar la tarea seleccionada?")
       if confirmar:
           treeview.delete(seleccion)




def agregar_tarea():
   tarea_nombre = cajadetexto.get() 
   if tarea_nombre:
       fecha_hoy = datetime.today()  # Obtener la fecha y hora actual  # Formatear la fecha
       treeview.insert("", tkinter.END, text=tarea_nombre, values=(fecha_hoy.strftime("%d/%m/%y"), False))
       cajadetexto.delete(0, tkinter.END)


def eliminar_tarea():
   menjaseEliminar = messagebox.askyesno("Eliminado", "¿Estas Seguro que quieres eliminar esta tarea?")       
   if menjaseEliminar:
      seleccion = treeview.selection()
      if seleccion:
          treeview.delete(seleccion)




def completar_tarea():
   menjaseCompletar = messagebox.askyesno("Completado", "¿Estas Seguro de completar esta tarea?")       
   if menjaseCompletar:
      seleccion = treeview.selection()
      if seleccion:
          treeview.item(seleccion, values=("11/09/23", True))


def salir_tarea():
   mensajesalir = messagebox.askyesno("salir", "¿Estas seguro que queres salir?")
   if mensajesalir:
    ventana.destroy()


treeview = ttk.Treeview(columns=("descri", "compl"))
treeview.heading("#0", text="nombre")
treeview.heading("descri", text="fecha de creacion")
treeview.heading("compl", text="realizado")


cajadetexto= tkinter.Entry(ventana,font= "helvetica 12")
boton_eliminar= tkinter.Button(ventana,text="eliminar",bg= "red", command= eliminar_tarea,width=20)
boton_agregar= tkinter.Button(ventana,text="agregar",bg= "light green", command= agregar_tarea,width=20)
boton_completar= tkinter.Button(ventana,text="completar",bg="pink", command= completar_tarea,width=20)
boton_salir= tkinter.Button(ventana,text="salir",bg= "sky blue", command= salir_tarea,width=20)


treeview.pack()
crear_tarea=tkinter.Label(text="Ingresar tarea:")
crear_tarea.pack()
cajadetexto.pack()
boton_agregar.pack(side=tkinter.LEFT)
boton_completar.pack(side=tkinter.LEFT)
boton_eliminar.pack(side=tkinter.LEFT)
boton_salir.pack(side=tkinter.LEFT)
ventana.mainloop()





