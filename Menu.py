import sqlite3

def menu():
    print("*************************************")
    print("               Menu                  ")
    print("*************************************")
    print("1. CONEXION CON BD")
    print("2. CREACION DE TABLA")
    print("3. BORRAR TABLA")
    print("4. INSERTAR DATOS EN TABLA")
    print("5. MOSTRAR DATOS DE TABLA")
    print("6. ACTUALIZAR REGISTRO DE TABLA")
    print("7. ELIMINAR DATO DE TABLA")
    print("0. SALIR")
    print(" Ingrese OPCION -----> ")

def opciones():
    opcion=input()
    if(opcion == "1"):
        conecta_bd()
        menu()
        opciones()
    elif (opcion == "2"):
        crear_Tabla()
        menu()
        opciones()
    elif (opcion == "3"):
        borrar_Tabla()
        menu()
        opciones()
    elif (opcion == "4"):
        insertarTabla()
        menu()
        opciones()
    elif (opcion == "5"):
        mostrarTabla()
        menu()
        opciones()
    elif (opcion == "6"):
        ActualizarTabla()
        menu()
        opciones()
    elif (opcion == "7"):
        eliminarTabla()
        menu()
        opciones()
    elif (opcion == "0"):
        exit()

def conecta_bd():
   bd = sqlite3.connect("libros.db")
   print("Base de datos abierta")

def crear_Tabla():
    try:
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()
        tablas = [
        """
        CREATE TABLE IF NOT EXISTS libros(
        autor TEXT,
        genero TEXT,
        precio REAL,
        titulo REAL
        );
        """
    ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

def borrar_Tabla():
    try:
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()
        tablas = [
        """
        DROP TABLE libros
        """
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas borradas correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

def insertarTabla():
    try:
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()
        libros = [
        """
        INSERT INTO libros
        (autor,genero,precio,titulo)
        VALUES
        ('Stephen King', 'Terror', 115, 'Cementario de animales'),
        ('Alfred', 'Ciencia Ficcion', 200, 'Las estrellas mi destino'),
        ('Margaret', 'Ciencia Ficcion', 150, 'El cuento de la criada');
        """
        ]
        for sentencia in libros:
            cursor.execute(sentencia)
        bd.commit()
        print("Libros insertados correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

def mostrarTabla():
    try:
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()
        sentencia = "SELECT * FROM libros;"

        cursor.execute(sentencia)

        libros = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}+".format("Autor","Genero","Precio","Titulo"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
                       
        for (autor,genero,precio,titulo) in libros:
            print("|{:^20}+{:^20}+{:^10}+{:^50}+".format(autor,genero,precio,titulo))
    
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

def ActualizarTabla():
    try:
        # Conectar a la base de datos
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()

        # Listar los libros
        sentencia = "SELECT *,rowid FROM libros;"

        cursor.execute(sentencia)

        libros = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10        }+".format("Autor", "Genero", "Precio", "Titulo", "RowID"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

        for autor, genero, precio, titulo, rowid in libros:
            print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}+".format(autor, genero, precio, titulo, rowid))

        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

        #Pedir ID del libro a editar
        id_libro = input("\nEscriba el ID del Libro que quiere editar: ")
        if not id_libro:
            print("No escribio nada")
            exit()
    
        #Pedir nuevos datos
        autor = input("\nNuevo Autor: ")     
        genero = input("\nNuevo Genero: ")
        precio = input("\nNuevo Precio: ")
        titulo = input("\nNuevo Titulo: ")

        #Sentencia para actualizar 
        sentencia = "UPDATE libros SET autor = ?, genero = ?, precio = ?, titulo = ? WHERE rowid = ?;"

        #Actualizar Datos
        cursor.execute(sentencia, [autor, genero, precio, titulo, id_libro])
        bd.commit()
        print("Datos Guardados")

    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

def eliminarTabla():
    try:
        # Conectar a la base de datos
        bd = sqlite3.connect("libros.db")
        cursor = bd.cursor()

        # Listar los libros
        sentencia = "SELECT *,rowid FROM libros;"

        cursor.execute(sentencia)

        libros = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
        print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}+".format("Autor", "Genero", "Precio", "Titulo", "RowID"))
        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

        for autor, genero, precio, titulo, rowid in libros:
            print("|{:^20}+{:^20}+{:^10}+{:^50}+{:^10}+".format(autor, genero, precio, titulo, rowid))

        print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))

        #Pedir ID del libro a editar
        id_libro = input("\nEscriba el ID del Libro que quiere eliminar: ")
        if not id_libro:
            print("No escribio nada")
            exit()
    
        #Sentencia para actualizar 
        sentencia = "DELETE FROM libros WHERE rowid = ?;"

        #Actualizar Datos
        cursor.execute(sentencia, [id_libro])
        bd.commit()
        print("Datos Eliminados")

    except sqlite3.OperationalError as error:
        print("Error al abrir", error)

menu()
opciones()