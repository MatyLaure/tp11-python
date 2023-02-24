import sqlite3

conectar = sqlite3.connect('trabajoPractico11.db')

cursor = conectar.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Matias', 'Garcia')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Jpnathan', 'Retamal')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Miguel', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Jorge', 'Orozco')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Javier', 'Ibarra')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Matias', 'Laure')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Andres', 'Mamani')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Rolo', 'Puentes')")

conectar.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Matias'")

filas = cursor.fetchall()

print(filas)

conectar.close()