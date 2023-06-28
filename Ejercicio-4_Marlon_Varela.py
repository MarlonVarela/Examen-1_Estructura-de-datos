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

def mayorvalor_arreglo():
    mayor = max(arreglo)
    label3.config(text=str(mayor))


def menorvalor_arreglo():
    menor = min(arreglo)
    label4.config(text=str(menor))

ventana = tk.Tk()
ventana.geometry("450x350")
ventana.title("Ejercicio 4")

#Este cuenta como el tamaño del arreglo
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

button_tamaño_arreglo = tk.Button(ventana, text = "Mostrar tamaño del arreglo", command=tamaño_arreglo)
button_tamaño_arreglo.pack()

label5 = tk.Label(ventana,  text = " ")
label5.pack()

label6 = tk.Label(ventana,  text = " ")
label6.pack()

#Este label lo cree para crear espacios entre los elementos de la ventana
labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

button_mayorvalor = tk.Button(ventana, text = "Mostrar el elemento de Mayor Valor", command=mayorvalor_arreglo)
button_mayorvalor.pack()

label3 = tk.Label(ventana, text = " ")
label3.pack()

#Este label lo cree para crear espacios entre los elementos de la ventana
labelinv = tk.Label(ventana, text= " ")
labelinv.pack()

button_menorvalor = tk.Button(ventana, text = "Mostrar el elemento de Menor Valor", command=menorvalor_arreglo)
button_menorvalor.pack()

label4 = tk.Label(ventana, text = " ")
label4.pack()

arreglo = []

ventana.mainloop()
