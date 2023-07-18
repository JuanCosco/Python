import sqlite3

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
