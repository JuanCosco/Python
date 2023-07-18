import sqlite3

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
