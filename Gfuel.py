import random
#Importamos solo las funciones que queremos
from DataSQL import Inicialize_List_Gfuels, query
import tkinter as tk

#una lista bascia
gFuel = []


def CuantosRicosGFuels():
    #len() devuelve el tamaño de lo que le pases en nuestro caso cuantos elemento en la lista
    return len(gFuel)

#Este es el subprograma principal de este fichero
def randomGFuel(label1):
    '''
    Para utilizar un .txt hay que pasarle la direccion o el nombre si esta en la misma carpeta
    y el modo en el que se va a abrir, es importante elegir el modo apropiado por que distintos modos
    leen y escriben distinto sobre el fichero
    '''
    ult = open("text.txt", "r")
    #Linea por linea lee el txt
    ricosGFuels = ult.readlines()
    #con la base de datos llenamos nuestras lista
    Inicialize_List_Gfuels(gFuel)
    
    '''
    Si el txt estaba vacio lo inicializamos de manera aleatoria.
    El txt guarda el nombre de las dos ultimas bebidas y al final un 1 o un 0,
    este numero nos dice si la ultima bebida esta en la linea 0 o en la 1 y por
    lo tanto cambiaremos la otra linea
    '''
    if len(ricosGFuels) == 0:
        #Si esta vacio añadidos dos aleatorios y un 0
        ult.write(gFuel[random.randint(0,CuantosRicosGFuels()-1)] )
        ult.write(gFuel[random.randint(0,CuantosRicosGFuels()-1)])
        ult.write("0\n")
        #Guardar los cambios
        ult.truncate()
        #guardamos los que hemos añadidos
        ricosGFuels = ult.readlines()
   
    #Una bebida aleatoria 
    a = gFuel[random.randint(0,CuantosRicosGFuels()-1)]   
    #mientras toque una que este entre las dos ultimas volvemos a hacerlo
    while ricosGFuels[0] == a or ricosGFuels[1] == a:
        a = gFuel[random.randint(0,CuantosRicosGFuels()-1)]
    
    #guardar donde se metio la ultima bebida
    pos = int(ricosGFuels[2])
    #si era 0 cambiamos a uno si era 1 a 0
    posInsertion = abs(pos-1)
    #en la posicion que toca añadidos el nuevo
    ricosGFuels[posInsertion] = a
    #para escribirlo bien tenemos que combertirlo a string
    ricosGFuels[2] = str(posInsertion)
    print(ricosGFuels)
    #cerramos el fichero en modo lectura
    ult.close()
    #abrimos en modo escritura
    ult = open("text.txt", "w")
    #escribe linea por linea cada elemento de la lista
    ult.writelines(ricosGFuels) 
    ult.truncate()
    ult.close()
    #sacamos en pantalla usando la etiqueta que nos han pasado el nombre
    label1.configure(text = a)
    #se devuelve por si se quiere usar para otra cosa
    return a

#añade otro sabor a la base de datos
def add(t):
    text = t.get()
    text = text +" \n"
    query('INSERT INTO gfuel VALUES (?)',text)
    gFuel.append(text)
    
def eliminar(t,l):
    
        text = t.get()
        text = text +" \n"
        query('DELETE FROM gfuel WHERE name = ?', text)
        l.configure(text = 'Sabor eliminado')
    
    

def iniciarVentana():
    #gestor de TKinter para este fichero, como es independiente puede funcioanr aun cerrando los otros
    gfuelWindow = tk.Tk()
    gfuelWindow.title('GFuel Central')
    canvas1 = tk.Canvas(gfuelWindow, width = 350, height = 280)
    canvas1.pack()
    
    #Etiqueta donde aparecera el sabor
    label1 = tk.Label(gfuelWindow, text = "Tu GFuel aparecera aqui", fg='maroon1', font=('helvetica', 12, 'bold'))
    canvas1.create_window(175, 75, window=label1)
    #Este boton ejecutara la funcion que elige el sabor, usamos ' lambda : ' en command para que nos deje pasar parametros
    button1 = tk.Button(gfuelWindow,text='Dame mi rico GFuel',command = lambda : randomGFuel(label1), bg='blue',fg='white')
    canvas1.create_window(175,115,window = button1)
    
    #un entry es un sitio donde el usuario podra escribir, este se usara para añadir sabores a la base de datos
    textArea = tk.Entry(gfuelWindow)
    canvas1.create_window(175,170,window = textArea)
    
    #ejecuta la funcion de añadir un sabor a la base de datos usando lo escrito por el usuario
    addButton = tk.Button(gfuelWindow,text= 'Nuevo GFuel', command = lambda: add(textArea), bg='brown',fg='white' )
    canvas1.create_window(75,210, window = addButton)
    
    #Boton para eliminar uno de los sabores ya insertados usando la misma ventana de escritura que el add
    delButton = tk.Button(gfuelWindow,text= 'Borrar GFuel', command = lambda: eliminar(textArea,label1), bg='brown',fg='white' )
    canvas1.create_window(275,210, window = delButton)
    
    #Usando mainloop volvemos a conseguir que esta ventana sea independiente de las otras
    gfuelWindow.mainloop()