import tkinter as tk

root = tk.Tk()
root.geometry("350x300")

class Ejercicio_2:
    def __init__(self, root):
        self.root = root
        self.arreglo = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        
        self.label1 = tk.Label(self.frame, text="Elementos: ")
        self.label1.pack()
        
        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        #Este label lo cree para crear espacios entre los elementos de la ventana
        self.labelinv = tk.Label(self.frame, text = " ")
        self.labelinv.pack()
        
        self.button = tk.Button(self.frame, text="Encolar", command=self.encolar_elemento)
        self.button.pack()

        self.labelinv = tk.Label(self.frame, text = " ")
        self.labelinv.pack()
        
        self.desencolar_button = tk.Button(self.frame, text="Descolar", command=self.descolar_elemento)
        self.desencolar_button.pack()

        self.label2 = tk.Label(self.frame, text = " ")
        self.label2.pack()

        self.labelinv = tk.Label(self.frame, text = " ")
        self.labelinv.pack()

        self.button_tamaño_arreglo = tk.Button(self.frame, text = "Mostrar tamaño de la cola", command=self.tamaño_arreglo)
        self.button_tamaño_arreglo.pack()

        self.label3 = tk.Label(self.frame, text = " ")
        self.label3.pack()

        self.label4 = tk.Label(self.frame, text = " ")
        self.label4.pack()
    
    def encolar_elemento(self):
        elemento = self.entry.get()
        self.arreglo.append(elemento)
        self.label1["text"] = "Elementos: " + ", ".join(self.arreglo)
        self.entry.delete(0, tk.END)
        self.label2.config(text = str(" "))
        self.label3.config(text = str(" "))
        self.label4.config(text = str(" "))
        

    
    def descolar_elemento(self):
        self.label2.config(text = str(" "))
        self.label3.config(text = str(" "))
        self.label4.config(text = str(" "))
        if self.arreglo:
            primer_elemento = self.arreglo.pop(0)
            self.label1["text"] = "Elementos: " + ", ".join(self.arreglo)
        else:
            self.label2.config(text=str("La cola está vacia."))

    def tamaño_arreglo(self):
        tamaño = len(self.arreglo)
        self.label3.config(text = str("El tamaño de la cola es de: "))
        self.label4.config(text = str(tamaño))

 
    
if __name__ == "__main__":
    
    ventana = Ejercicio_2(root)
    
    root.mainloop()
