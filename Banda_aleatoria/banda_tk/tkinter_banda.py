import tkinter as tk
from tkinter import PhotoImage

def activate_photo(instrumentos):
    root = tk.Tk()
    root.title("Instrument Viewer")

    imagenes=[]
    for i in range(len(instrumentos)):
        imagen=PhotoImage(file=instrumentos[i])
        imagenes.append(imagen)

    for img in imagenes:
        label = tk.Label(root, image=img)
        label.pack()
    root.mainloop()


