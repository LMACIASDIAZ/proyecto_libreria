
from revista import Revista
from libro import Libro
from docente import Docente
from estudiante import Estudiante

class Pedido():
    contador_pedido = 0

    def __init__(self, solicitante, lista_material ,fecha_prestamo ,fecha_devolucion):
        Pedido.contador_pedido += 1
        self._id = Pedido.contador_pedido
        self._solicitante = solicitante
        self._lista_material = lista_material
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion


    def pedir_material(list_materia, estudiante_docente, materia):
        pass


    def devolver_material(estudiante_docente):
        pass