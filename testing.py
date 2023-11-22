import tkinter as tk

def scroll_text(event):
    canvas.xview_scroll(-1 * (event.delta // 120), "units")

root = tk.Tk()
root.title("Scroll de una Línea de Texto")

# Crear un lienzo (canvas) y una barra de desplazamiento horizontal
canvas = tk.Canvas(root, width=300, height=20, scrollregion=(0, 0, 500, 20), xscrollcommand=None)
hbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
canvas.config(xscrollcommand=hbar.set)

# Agregar texto al lienzo
texto = "Tu línea de texto larga aquí. Tu línea de texto larga aquí. Tu línea de texto larga aquí."
canvas.create_text(2, 4, anchor="w", text=texto)

# Configurar eventos de desplazamiento con la rueda del ratón
canvas.bind("<MouseWheel>", scroll_text)

# Colocar el lienzo y la barra de desplazamiento en la ventana
root.grid_rowconfigure(0, weight = 1)
canvas.grid(row=1, column=0, sticky="ew")
hbar.grid(row=2, column=0, sticky="ew")

root.mainloop()


