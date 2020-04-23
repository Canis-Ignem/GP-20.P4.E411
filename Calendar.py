import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
import DataSQL


def conteo(label1, label2, label3):
    
    e =DataSQL.query1Res('SELECT COUNT(exito) FROM exitos WHERE exito = "E"')
    f =DataSQL.query1Res('SELECT COUNT(exito) FROM exitos WHERE exito = "F"')
    label1.configure(text = e )
    label2.configure(text = '/' )
    label3.configure(text = f )
    
def insertDate(de,label1,label2,label3,combo):
    #de la fecha cogemo en modo string cada apartado
    d =str(de.get_date().day) 
    m =str(de.get_date().month)
    y =str(de.get_date().year)
    #y de la combobox el objeto seleccionado
    e = str(combo.get())
    
    #Podemos hacer una sentencia SQL usando parametros con el valor ? y despues 
    #pasandole los parametros aparte usando nuestra funcion de la base de datos
    DataSQL.query("INSERT INTO exitos VALUES (?, ?, ?, ?)",(d,m,y,e))
    
    conteo(label1,label2,label3)
    #commit para que se guarden los cambios
    DataSQL.conn.commit()

def inicicializeCalendar():
    
    calendar = tk.Tk()
    calendar.title("Calendar")
    
    #Vinculamos nuestro estilo con la ventana
    style = ttk.Style(calendar)
    #para usar un calendario desplegable es recomendable usar clam
    style.theme_use('clam')
    
    #la ventana visible para nosotros
    calendarCanvas = tk.Canvas(calendar,width= 500,height = 500)
    
    #Una etiqueta para mostrar la fecha
    label1 = tk.Label(calendar)
    calendarCanvas.create_window(260,350,window= label1)
    label1.configure( fg='green2',font=('helvetica', 20, 'bold') )
    
    
    
    label2 = tk.Label(calendar)
    calendarCanvas.create_window(300,350,window= label2)
    label2.configure( fg='black',font=('helvetica', 28, 'bold') )
    
    label3 = tk.Label(calendar)
    calendarCanvas.create_window(340,350,window= label3)
    label3.configure( fg='red2',font=('helvetica', 20, 'bold') )
    
    conteo(label1,label2,label3)
    
    #Un combobos es basicamente una lista desplegable esta nos permitira marcar los
    #dias como exito o fracaso y de esta manera hacernos responsables de lo que hacemos
    #cada dia
    exitoFracaso= ttk.Combobox(calendar,values=["E","F"],width = 5)
    calendarCanvas.create_window(100,350,window=exitoFracaso)
    exitoFracaso.current(0)
    
    #Este es el codigo que nos personaliza el calendario a nuestro gusto
    #Podemos ejegir el formato de la fecha los colores y como interactua con el raton
    cal = DateEntry(calendar, year=date.today().year, month=date.today().month, day=date.today().day,
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
    
    #organizar todo
    calendarCanvas.pack()
    #main loop para que sea independiente
    calendar.mainloop()