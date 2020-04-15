import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date


def inicializeCalendar():
    
    calendar = tk.TK()
    calendar.title("Calendar")
    
    #Vinculamos nuestro estilo con la ventana
    style = ttk.Style(calendar)
    #para usar un calendario desplegable es recomendable usar clam
    style.theme_use('clam')
    
    #la ventana visible para nosotros
    calendarCanvas = tk.Canvas(calendar,width= 500,height = 500)
    
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