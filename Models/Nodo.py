# Clase NODO --> es la que maneja los datos de cada peaje
class Nodo:
    # Constructor: (llave, valor, hijoIzquierdo, hijoDerecho, padre)
    def __init__(self, nombre, id, valor, nivel,recargoIzquierdo,recargoDerecho,categoria, padre=None, hijoIzquierdo=None, hijoDerecho=None):
        self.nombre = nombre
        self.id = id
        self.valor = valor
        self.nivel = nivel
        self.categoria = categoria
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho
        self.recargoIzquierdo = recargoIzquierdo
        self.recargoDerecho = recargoDerecho
        self.padre = padre
        self.bandera = True
        self.autosPeajes = []
        self.pagos = []

    #Obtiene el valor de 
    def getValue(self):
        return self.valor

    # Retornar el nodo del hijo izquierdo [None cuando no tiene hijo]
    def ObtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    # Asignar el nodo del hijo izquierdo
    def PonerHijoIzquierdo(self, hijo):
        self.hijoIzquierdo = hijo

    # Retornar el nodo del hijo derecho [None cuando no tiene hijo]
    def ObtenerHijoDerecho(self):
        return self.hijoDerecho

    # Asignar el nodo del hijo derecho
    def PonerHijoDerecho(self, hijo):
        self.hijoDerecho = hijo

    def ObtenerCategoria(self):
        return self.categoria

    def ObtenerRecargoIz(self):
        return self.recargoIzquierdo

    def ObtenerRecargoDe(self):
        return self.recargoDerecho

    def PonerPadre(self, padre):
        self.padre = padre

    def ObtenerPadre(self):
        return self.padre

    # Validar sí el nodo es raíz
    def EsNodoRaiz(self):
        return not self.padre

    # Validar sí el nodo es hoja
    def EsNodoHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)

    # obtener el nivel del nodo
    def ObtenerNivel(self):
        return self.nivel

    # Valida sí es hijo izquierdo
    def EsHijoIzquierdo(self):
        if (self.padre):
            if self.padre.ObtenerHijoIzquierdo():
                return self.valor == self.padre.ObtenerHijoIzquierdo().valor

    #Valida sí es hijo derecho
    def EsHijoDerecho(self):
        if (self.padre):
            if self.padre.ObtenerHijoDerecho():
                return self.valor == self.padre.ObtenerHijoDerecho().valor