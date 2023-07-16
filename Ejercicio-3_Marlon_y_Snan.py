import tkinter as tk

def agregar_elemento():
    label3.config(text = str(" "))
    label4.config(text = str(" "))
    label5.config(text = str(" "))
    label6.config(text = str(" "))

    elemento = int(entry1.get())
    arreglo.append(elemento)
    label2.config(text=str(arreglo))
    entry1.delete(0,tk.END)

def tamaño_arreglo():
    tamaño = len(arreglo)
    label5.config(text=str("El tamaño del arreglo es de: "))
    label6.config(text=str(len(arreglo)))

def suma_arreglo():
    suma = sum(arreglo)
    label3.config(text=str(suma))

def promedio_arreglo():
    suma = sum(arreglo)
    promedio = suma/len(arreglo)
    label4.config(text=str(promedio))

ventana = tk.Tk()
ventana.geometry("450x350")
ventana.title("Ejercicio 3")


label1 = tk.Label(ventana, text="Elementos del arreglo: ")
label1.pack()

label2 = tk.Label(ventana, text= " ")
label2.pack()

entry1 = tk.Entry(ventana)
entry1.pack()

button1 = tk.Button(ventana, text= "Agregar elemento", command=agregar_elemento)
button1.pack()

#Este label lo cree para crear espacios entre los elementos de la ventana
labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

button_tamaño_arreglo = tk.Button(ventana, text = "Mostrar tamaño de los elementos", command=tamaño_arreglo)
button_tamaño_arreglo.pack()

label5 = tk.Label(ventana,  text = " ")
label5.pack()

label6 = tk.Label(ventana,  text = " ")
label6.pack()

#Este label lo cree para crear espacios entre los elementos de la ventana
labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

button_suma = tk.Button(ventana, text = "Mostrar suma de los elementos", command=suma_arreglo)
button_suma.pack()

label3 = tk.Label(ventana, text = " ")
label3.pack()

#Este label lo cree para crear espacios entre los elementos de la ventana
labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

button_promedio = tk.Button(ventana, text = "Mostrar promedio de los elementos", command=promedio_arreglo)
button_promedio.pack()

label4 = tk.Label(ventana, text = " ")
label4.pack()

arreglo = []

ventana.mainloop()
