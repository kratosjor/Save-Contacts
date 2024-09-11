import sqlite3
import os #sirve para limpiar pantalla

def ingreso_str(mensaje, error):
    dato = input(mensaje)
    while dato == "":
        print(error)
        dato = input(mensaje)
    return dato

def guardar_contacto(nombre,telefono,email,direccion):
    try:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contactos VALUES (NULL,?,?,?,?)",(nombre,telefono,email,direccion))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactos (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre    TEXT,
                telefono  TEXT,
                email     TEXT,
                direccion TEXT
                       
            )
            """)
        cursor.execute("INSERT INTO contactos VALUES (NULL,?,?,?,?)",(nombre,telefono,email,direccion))
        conn.commit()
        conn.close()
    print("Se guardo el nuevo contacto!")

def mostrar_contactos():
    try:
        conn = sqlite3.connect("datos.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contactos;")
        contactos = cursor.fetchall()
        conn.close()

        if contactos:
            print("\nContactos guardados: ")
            for contacto in contactos:
                print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}, Email: {contacto[3]}, Dirección: {contacto[4]}")
        else:
            print("no hay contactos guardados.")

    except sqlite3.OperationalError:
        print("No se ha encontrado la base de datos o la table de contactos.")

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

salir = True



while salir:
    limpiar_pantalla()
    print("Menú:\n1. Ingreso de nuevo contacto\n2. Ver contactos guardados\n3. Salir")
    opcion = ingreso_str(">>>","Error, opcion no valida.")
    
    if opcion == "1":
        limpiar_pantalla()
        nombre = ingreso_str("Ingrese el nombre: ","Error, este campo no debe estar vacio.")
        telefono = ingreso_str("Ingrese el telefono de contacto: ","Error, este campo no debe estar vacio.")
        email = ingreso_str("Ingrese el email de contacto: ","Error, este campo no debe estar vacio.")
        direccion = ingreso_str("Ingrese direccion: ","Error, este campo no debe estar vacio.")
        guardar_contacto(nombre,telefono,email,direccion)
        input("\nPresione ENTER para volver al Menu.......")

    elif opcion == "2":
        limpiar_pantalla()
        print("Datos Guardados.")
        mostrar_contactos()
        input("\nPresione ENTER para volver al Menu.......")
        
    elif opcion == "3":
        print("Gracias por usar el programa.")
        salir = False
    else:
        print("Opcion no valida.")
        input("\nPresione ENTER para volver al Menu.......")
    



