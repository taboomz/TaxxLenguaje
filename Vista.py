from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
import taxxLexico
from taxxLexico import Taxx

class Aplicacion:
        def __init__(self):
                self.raiz=Tk()
                self.raiz.title("TAXX")
                self.agregar_menu()
                self.scrolledtext1=st.ScrolledText(self.raiz,width=100,height=30)
                self.scrolledtext1.grid(column=0,row=0, padx=10, pady=10)
                self.raiz.mainloop()


        def agregar_menu(self):
                barraMenu=Menu(self.raiz)
                self.raiz.config(menu=barraMenu, width="300", height="250")
                archivoMenu=Menu(barraMenu,tearoff="0")
                archivoMenu.add_command(label="Cargar",command=self.codigoCargar)
                archivoMenu.add_command(label="Guardar",command=self.codigoGuardar)

                ejecutarMenu=Menu(barraMenu,tearoff="0")
                ejecutarMenu.add_command(label="Ejecutar Lex",command=self.ejecutarLex)
                ejecutarMenu.add_command(label="Ejecutar Pars")


                informacionMenu=Menu(barraMenu,tearoff="0")
                informacionMenu.add_command(label="informacion",command=self.informacion)


                barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
                barraMenu.add_cascade(label="Ejecutar",menu=ejecutarMenu)
                barraMenu.add_cascade(label="Info", menu=informacionMenu)

        def informacion(self):
                messagebox.showinfo("INFORMACION","Compiladores 2019- Grupo 2 \n 2012214076")

        def codigoGuardar(self):
                nombrearch=fd.asksaveasfilename(initialdir="/Desktop/",title="Guardar como",filetypes=(("taxx files","*.taxx"),("todos los archivos","*.*")))
                if nombrearch != '':
                        guardar=open(nombrearch,"w",encoding="utf-8")
                        guardar.write(self.scrolledtext1.get("1.0",END))
                        guardar.close()
                        messagebox.showinfo("Información", "Los datos fueron guardados en el archivo.")
        def codigoCargar(self):
                nombrearch=fd.askopenfilename(initialdir="/Desktop/",title="Seleccione archivo",filetypes=(("taxx files", "*.taxx"),("todos los archivos","*.*" )) )
                if nombrearch != '':
                        archi1=open(nombrearch, "r", encoding="utf-8")
                        contenido=archi1.read()
                        archi1.close()
                        self.scrolledtext1.delete("1.0", END)
                        self.scrolledtext1.insert("1.0", contenido)

        def ejecutarLex(self):
                archivo=fd.askopenfilename(initialdir="/Desktop/",title="Seleccione archivo",filetypes=(("taxx files", "*.taxx"),("todos los archivos","*.*" )) )
                if archivo != '':
                        archi1=open(archivo, "r", encoding="utf-8")
                        contenido=archi1.read()
                        archi1.close()
                #archivo="/Users/TavoMZ/Desktop/Lenguaje Taxx/prueba/"
                        lexico=Taxx()
                        lexico.compilar(archivo)

aplicacion1=Aplicacion()
