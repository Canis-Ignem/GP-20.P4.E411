import sqlite3 as sql

'''
Este fichero es el controlador de la base de datos, se debe evitar  importar otros ficheros para evitar imports circulares

conn es la conexion con nuestra base de datos

c es el elemento desde el cual ejecutaremos nuestras sentencias y recibiremos nuestros resultados
'''

#Database.db se crea si no existe con el connect
conn = sql.connect('DataBase.db')
c = conn.cursor()

#Necesitamos rodearlo en un try/except para evitar errores de tablas creadas y elementos ya creados
def inicialize():
    try:
        
        # en el execute puedes meter cualquier sentencia SQL
        c.execute('''CREATE TABLE IF NOT EXISTS gfuel
                    (name text PRIMARY KEY)''')
        c.execute('''CREATE TABLE IF NOT EXISTS exitos
                    (dday text, mmonth text, yyear text, exito text)
                  ''')

        #Gfuel es solo una bebida que me gusta a mi y viene en sabores podria cambiarse por comidas o cualquier otra cosa
        #Usaremos los gfuels para aprender a operar ficheros txt para evitar repeticiones por eso es importante añadir el salto de linea al final
        c.execute("INSERT INTO gfuel VALUES ('Grape \n') ")
        c.execute("INSERT INTO gfuel VALUES ('Peach Mango \n') ")
        c.execute("INSERT INTO gfuel VALUES ('Kiwi Strawebrry \n') ")
        c.execute("INSERT INTO gfuel VALUES ('Frut Chug Rug \n') ")
        c.execute("INSERT INTO gfuel VALUES ('Battle Juice \n') ")
        c.execute("INSERT INTO gfuel VALUES ('Watermelon \n') ")
        #sin commit los cambios no se guardan
        conn.commit()
    except:
        print("Table already created")
    
#Cada elemento de la base de datos de GFuel puede ser añadido a una lista, sin embargo text de SQL no es compatible con str de python
#es importante hacer la conversion
def Inicialize_List_Gfuels(list):
    if len(list) == 0: 
        for row in c.execute("SELECT NAME FROM gfuel"):
            aux = str(row)
            #puedes coger un subapartado de un string de esta manera
            aux = aux[2:len(aux)-6]+" \n"
            list.append(aux)
    else:
        print("list is already inicialized")

#ejecutara la sentencia que se pase por paramentro en senctence con los parametros pasados en data ya,
# para usar la base de datos desde otras clases se usara esta funcion
# cada elemento de data se sustituira en los '?' que haya en la sentencia, esta funcion es polivalente 
def query(sentence ,data):
    if type(data) is str:
        c.execute( sentence , (data,))
         
    else:
        c.execute( sentence , data)
        
    conn.commit()

