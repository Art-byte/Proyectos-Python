import pymysql
class Bases():
    
    def consulta():
        db = pymysql.connect(   host = 'localhost',port = 3307,user = 'root',
                                passwd = 'Lanochemasoscura',db = 'Usuarios')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        data = cursor.fetchall()
        for i in data:
            print("\n",i)
        db.close()
        
    def consultaMacho():
        db = pymysql.connect( host = 'localhost',port = 3307,user = 'root',
                             passwd = 'Lanochemasoscura',db = 'Usuarios')
        cursor = db.cursor()
        cursor.execute("SELECT count(sexo) FROM Usuarios WHERE sexo = 'Masculino'")
        data = cursor.fetchall()
        print("\n")
        print("¿Cuantos hombres hay?")
        print("Existen en total: ",data," de hombres")
        db.close()
        
    def consultaHembra():
        db = pymysql.connect(host = 'localhost',port = 3307,user = 'root',
                             passwd = 'Lanochemasoscura',db = 'Usuarios')
        cursor = db.cursor()
        cursor.execute("SELECT count(sexo) FROM Usuarios WHERE sexo = 'Femenino'")
        data = cursor.fetchall()
        print("\n")
        print("¿Cuantas Mujeres hay?")
        print("Existen en total: ",data," de Mujeres")
        
        db.close()
        
    def ConsultaEstado():
        db = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root',
            passwd = 'Lanochemasoscura',
            db = 'Usuarios'
        )
        cursor = db.cursor()
        cursor.execute("SELECT count(sexo), EDO_PROV  FROM Usuarios group by EDO_PROV" )
        data = cursor.fetchall()
        print("\n")
        print("¿Cuantas personas hay por estado?")
        print(data)
        db.close()
        
        
        
        
    def CuantosVatos():
        db = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root',
            passwd = 'Lanochemasoscura',
            db = 'Usuarios'
        )
        cursor = db.cursor()
        cursor.execute("SELECT EDO_PROV, count(sexo) from Usuarios where sexo = 'Masculino' group by EDO_PROV")
        data = cursor.fetchall()
        print("\n")
        print("Existen esta cantidad de personas Masculinas por estado: ")
        print(data) 
        db.close()
        
        
    def CuantosMorras():
        db = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root',
            passwd = 'Lanochemasoscura',
            db = 'Usuarios'
        )
        cursor = db.cursor()
        cursor.execute("SELECT EDO_PROV, count(sexo) from Usuarios where sexo = 'Femenino' group by EDO_PROV")
        data = cursor.fetchall()
        print("\n")
        print("Existen esta cantidad de personas Femeninas por estado: ")
        print(data) 
        db.close()
        
    def EdadHombres():
        db = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root',
            passwd = 'Lanochemasoscura',
            db = 'Usuarios'
        )
        cursor = db.cursor()
        cursor.execute("SELECT nombre, year(fecha_nacimiento) - 2019 as Edad_de_los_morros from usuarios where sexo = 'Masculino' order by Fecha_Nacimiento DESC")
        data = cursor.fetchall()
        print("\n")
        print("La edad de los hombres es: ")
        print(data)
        db.close()
        
    def EdadMujeres():
        db = pymysql.connect(
            host = 'localhost',
            port = 3307,
            user = 'root',
            passwd = 'Lanochemasoscura',
            db = 'Usuarios'
        )
        cursor = db.cursor()
        cursor.execute("SELECT nombre, year(fecha_nacimiento) - 2019 as Edad_de_las_morras from usuarios where sexo = 'Femenino' order by Fecha_Nacimiento DESC")
        data = cursor.fetchall()
        print("\n")
        print("La edad de las mujeres es: ")
        print(data)
        db.close()
        

#totalRegistros = Bases.consulta()
TotalMasculino = Bases.consultaMacho()
TotalHembras = Bases.consultaHembra()
PerXEstado = Bases.ConsultaEstado()
VatosEstado = Bases.CuantosVatos()
MorrasEstado = Bases.CuantosMorras()
EdadHembra = Bases.EdadMujeres()
EdadMacho = Bases.EdadHombres()