import tkinter as tk
from tkinter import ttk
import tkcalendar
import datetime
import DataSQL
from tkinter import messagebox
#Este impor es debido a un error al conseguir el .exe, sin el no es capaz de añadir las clases necesarias
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *  # Additional Import


#Una funcion para contar los exitos y los fracasos segun la cantidad de estos que haya en la base de datos
def conteo(label1, label2, label3):
    #Contrar exitos y fracasos
    e =DataSQL.query1Res('SELECT COUNT(exito) FROM exitos WHERE exito = "E"')
    f =DataSQL.query1Res('SELECT COUNT(exito) FROM exitos WHERE exito = "F"')
    #Actualizar las labels
    label1.configure(text = e )
    #label2.configure(text = '/' )
    label3.configure(text = f )
    
def insertDate(de,label1,label2,label3,combo):
    #de la fecha la cogemos en modo string cada apartado
    d =str(de.get_date().day) 
    m =str(de.get_date().month)
    y =str(de.get_date().year)
    #y de la combobox el objeto seleccionado
    e = str(combo.get())
    
    #Podemos hacer una sentencia SQL usando parametros con el valor ? y despues 
    #pasandole los parametros aparte usando nuestra funcion de la base de datos
    DataSQL.query("INSERT INTO exitos(dday,mmonth,yyear,exito) VALUES (?, ?, ?, ?)",(d,m,y,e))
    
    conteo(label1,label2,label3)
    #commit para que se guarden los cambios
    DataSQL.conn.commit()

#Una funcion que nos permita guardar o lo los cambios al salir de las notas
def closing(chores,d,m,y,t):
    #Una ventana con para dar el OK o cancelarlo que devuelve true si se ha elegdo el si
    if messagebox.askokcancel("Salir", "Desea guardar los cambios?"):
        #actuaizamos las tareas de ese dia
        DataSQL.query("UPDATE exitos SET tareas = ? WHERE dday = ? and mmonth = ? and yyear = ?", (t,d,m,y))
    chores.destroy()
    
def notas(de):
    #Nueva ventana por comodidad de escritura
    chores = tk.Tk()
    chores.title('Chores')
    #Text sirve como punto de texto que el usuario puede editar, si lo definimos asi toda la ventana sera de tipo texto
    choresT = tk.Text(chores)
    #Coger la fecha seleccionada
    d =str(de.get_date().day) 
    m =str(de.get_date().month)
    y =str(de.get_date().year)
    #Guardamos las tareas de esa fecha en una variable
    text = str(DataSQL.query1ResParams("SELECT tareas FROM exitos WHERE dday = ? and mmonth = ? and  yyear = ?",(d,m,y)))
    #Al insertar le quitamos los parentesis y comillas y demases que viene con el cambio a str ('....\n')
    text = text[2:-5];
    lines = text.split('\\n')
    for i in range(len(lines)):
        choresT.insert(tk.INSERT,lines[i])
        choresT.insert(tk.INSERT,"\n")
        
    #Protocolo de cerrado de la ventana
    chores.protocol("WM_DELETE_WINDOW",lambda: closing(chores,d,m,y,choresT.get("1.0",tk.END) ) )
    choresT.pack()
    

def inicicializeCalendar():
    calendar = tk.Tk()
    calendar.title("Calendar")
    
    #Vinculamos nuestro estilo con la ventana
    style = ttk.Style(calendar)
    #para usar un calendario desplegable es recomendable usar clam
    style.theme_use('clam')
    
    #la ventana visible para nosotros
    calendarCanvas = tk.Canvas(calendar,width= 500,height = 500)
    
    choreCanvas = tk.Canvas(calendar,width= 1000, height = 1000)
    
    
    
    
    
    #Una etiqueta para mostrar la fecha
    label1 = tk.Label(calendar)
    calendarCanvas.create_window(260,350,window= label1)
    label1.configure( fg='green2',font=('helvetica', 20, 'bold') )
    
    
    #Etiquetas para mostrar los exitos y fracasos con colores
    label2 = tk.Label(calendar)
    calendarCanvas.create_window(300,350,window= label2)
    label2.configure( fg='black',text = '/',font=('helvetica', 28, 'bold') )
    
    label3 = tk.Label(calendar)
    calendarCanvas.create_window(340,350,window= label3)
    label3.configure( fg='red2',font=('helvetica', 20, 'bold') )
    
    #actualiza las aetiquetas tras cada insercion
    conteo(label1,label2,label3)
        
    
    #Un combobos es basicamente una lista desplegable esta nos permitira marcar los
    #dias como exito o fracaso y de esta manera hacernos responsables de lo que hacemos
    #cada dia
    exitoFracaso= ttk.Combobox(calendar,values=["E","F"],width = 5)
    calendarCanvas.create_window(100,350,window=exitoFracaso)
    exitoFracaso.current(0)
    
    #Este es el codigo que nos personaliza el calendario a nuestro gusto
    #Podemos ejegir el formato de la fecha los colores y como interactua con el raton
    
    cal = tkcalendar.DateEntry(calendar, year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day,
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70',
                 date_pattern='dd/MM/yy'
                 )
    
    # lo metemos en la ventana
    calendarCanvas.create_window(250,50,window = cal )
    
    #Un boton que ejecute la funcion de insercion a la BD
    aceptB= tk.Button(calendar,text='insert',command = lambda: insertDate(cal,label1,label2,label3,exitoFracaso))
    calendarCanvas.create_window(100,400, window=aceptB)
    
    #boton para las notas
    botonNotas = tk.Button(calendarCanvas,text = 'Tareas',command = lambda: notas(cal))
    calendarCanvas.create_window(400,400,window= botonNotas)

    #organizar todo
    calendarCanvas.pack()
    #main loop para que sea independiente
    calendar.mainloop()