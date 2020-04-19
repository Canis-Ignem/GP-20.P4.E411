import tkinter as tk
from DataSQL import inicialize
import Gfuel
import Calendar

#root sera nuestra controlador de TKinter principal y se inicializa asi
root = tk.Tk()
#Se le asigna un nombre
root.title('Hub')
#Esta es la ventana que nosotros veremos por pantalla
#Le decimos quien es el padre y sus dimensiones
mainCanvas = tk.Canvas(root, width = 500, height = 500)
#La funcion pack simplemente organiza las cosas automaticamente
#Aun que vayamos a colorcar las cosas manualmente merece la pena su uso
mainCanvas.pack()

#Usaremos esto como mascara para el boton de los gfuels
def openGFuels():
    Gfuel.iniciarVentana()

#Usaremos esto como mascara para el boton del calendario  
def openCalendar():
    Calendar.inicicializeCalendar()



#al arracar inicializamos la base de datos
inicialize()

#Para lanzar la aplicacion que te lleva a las bebidas creamos un boton que lo haga
buttonGFuel = tk.Button(root,text='GFuel lobby',command = openGFuels, bg='brown',fg='white')
mainCanvas.create_window(100,250,window = buttonGFuel)

#Para lanzar la aplicacion de calendario
calendarButton = tk.Button(root,text='Calendar lobby',command = openCalendar, bg='green',fg='white')
mainCanvas.create_window(400,250,window = calendarButton)

#Esto es una etiqueta normal y corriente se le especifica el padre el texto y la fuente
label = tk.Label(root, text = "Welcome", fg='maroon1', font=('helvetica', 20, 'bold'))
#createWindow nos sirve para colcar en nuestro "canvas" los widgets que ya hemos creado
mainCanvas.create_window(250, 50, window=label)
#este es el metodo que inicializa todo y lo ejecuta dejandolo funcionando hasta que cerremos la ventana
root.mainloop()