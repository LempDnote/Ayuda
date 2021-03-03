import NodoMatriz as Nodo
import Datos as dato

class Matriz():

    def __init__(self):
        self.inicio = None

    def Crear(self,n,m):
        q = None
        r = None
        for i in range(1,n+1):
            for j in range(1,m+1):
                nuevo = Nodo.Nod(dato.Datos("Hola","15"))
                nuevo.siguiente = None
                nuevo.abajo = None
                if j == 1:
                    nuevo.anterior = None
                    if self.inicio == None:
                        self.inicio = nuevo
                    q = nuevo
                else:
                    nuevo.anterior = q
                    q.siguiente = nuevo
                    q = nuevo
                if i == 1:
                    nuevo.arriba = None
                    q = nuevo
                else:
                    nuevo.arriba = r
                    r.abajo = nuevo
                    r = r.siguiente
                r = self.inicio
                while r.abajo != None:
                    r = r.abajo

    def Mostrar(self):
        if self.inicio != None:
            temp = self.inicio
            while temp.abajo != None:
                temp2 = temp
                while temp2 != None:
                    print(temp2.dato.nombre)
                    temp2 = temp2.siguiente
                temp = temp.abajo







