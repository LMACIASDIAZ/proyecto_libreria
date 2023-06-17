


    from revista import Revista
    from libro import Libro
    from docente import Docente
    from estudiante import Estudiante


    # Docentes
    d1 = Docente(cedula = '0000000001', nombre = 'JOSE', apellido= 'CORDOVA', email='jscordovaa@gmail.com', telefono='0982222920', direccion='LA JOYA', numero_libros=0, activo=True, carrera='ISAC', titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
    d2 = Docente(cedula = '0000000002', nombre = 'GUILLERMO', apellido= 'VALAREZO', email='gvalarezo@gmail.com', telefono='0909090909', direccion='s/n', numero_libros=0, activo=True, carrera='ISAC', titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
    print(d1)
    print(d2)

    # Estudiantes
    e1 = Estudiante(cedula = '0917236663', nombre = 'JOSE', apellido= 'CORDOVA', email='jscordovaa@gmail.com', telefono='0982222920', direccion='LA JOYA', numero_libros=0, activo=True, carrera='ISAC', nivel=1)
    e2 = Estudiante(cedula = '0917236663', nombre = 'JOSE', apellido= 'CORDOVA', email='jscordovaa@gmail.com', telefono='0982222920', direccion='LA JOYA', numero_libros=0, activo=True, carrera='ISAC', nivel=1)
    print(e1)
    print(e2)

    l1 = Libro(codigo='1', autor='', titulo='', anio=2019, editorial='', disponible=True, cantidad_disponible=10,tipo_pasta='')
    l2 = Libro(codigo='1', autor='', titulo='', anio=2019, editorial='', disponible=True, cantidad_disponible=10,tipo_pasta='')
    print(l1)