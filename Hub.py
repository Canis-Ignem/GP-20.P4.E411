import tkinter as tk


root = tk.Tk()
root.title('Hub')
mainCanvas = tk.Canvas(root, width = 500, height = 500)
mainCanvas.pack()


label = tk.Label(root, text = "Welcome", fg='maroon1', font=('helvetica', 20, 'bold'))
mainCanvas.create_window(250, 50, window=label)

root.mainloop()