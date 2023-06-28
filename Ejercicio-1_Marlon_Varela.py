import tkinter as tk

def agregar_elemento():
    elemento = int(entry1.get())
    arreglo.append(elemento)
    label2.config(text=str(arreglo))
    entry1.delete(0,tk.END)

def buscar_elemento():
    elemento = int(entry2.get())
    for index in range(len(arreglo)):
        if arreglo[index] == elemento:
             return "Elemento encontrado"
    return "Elemento no encontrado"

def buscar_elemento_click():
    label4.config(text=buscar_elemento())


ventana = tk.Tk()
ventana.geometry("450x300")
ventana.title("Ejercicio 1")

label1 = tk.Label(ventana, text="Ingrese un elemento al arreglo: ")
label1.pack()

entry1 = tk.Entry(ventana)
entry1.pack()

button1 = tk.Button(ventana, text= "Agregar elemento", command=agregar_elemento)
button1.pack()

label2 = tk.Label(ventana, text= "Resultado: ")
label2.pack()

label3 = tk.Label(ventana, text= "Elemento a buscar: ")
label3.pack()

entry2 = tk.Entry(ventana)
entry2.pack()

button2 = tk.Button(ventana, text= "Buscar elemento: ", command=buscar_elemento_click)
button2.pack()

label4 = tk.Label(ventana, text= " ")
label4.pack()

arreglo = []

ventana.mainloop()



