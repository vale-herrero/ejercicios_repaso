import random

class nodoArbol(object):
    def __init__(self,info):
        self.izq = None
        self.der = None
        self.info = info

def insertar_nodo(raiz, dato):
    if(raiz is None):
        raiz = nodoArbol(dato)
    elif(dato < raiz.info):
        raiz.izq = insertar_nodo(raiz.izq,dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def buscar(raiz,clave):
    pos = None
    if(raiz is not None):
        if(raiz.info == clave):
            pos = clave
        elif(clave < raiz.info):
            pos = buscar(raiz.izq,clave)
        else:
            pos = buscar(raiz.der,clave)
        return pos

def remplazar(raiz):
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminar_nodo(raiz,clave):
    x = None
    if( raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der,clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

def EsPar(numero):
    if(numero%2):
        return False
    else:
        return True
CantidadNumeros=1000
NumeroAleatorio = random.randint(0,CantidadNumeros)
Arbol = nodoArbol(NumeroAleatorio)
ContadorPares=0
ContadorImpares=0
for i in range(CantidadNumeros-1):
    NumeroAleatorio = random.randint(0,CantidadNumeros)
    if(EsPar(NumeroAleatorio)):
        ContadorImpares += 1
    else:
        ContadorPares += 1
    Arbol = insertar_nodo(Arbol, NumeroAleatorio)

print("Despliegue [1]Preorden [2]Inorden [3]Postorden: ")
Despliegue = int(input())
if(Despliegue==1):
    preorden(Arbol)
elif(Despliegue==2):
    inorden(Arbol)
elif(Despliegue==3):
    postorden(Arbol)
else:
    print("Orden no encontrada")

print("Buscar numero entero en el rango [0-1000]: ")
NumeroBuscar = int(input())
NumeroBuscado = buscar(Arbol,NumeroBuscar)
if(NumeroBuscado is not None):
    print('Numero {} se encuentra en el arbol'.format(NumeroBuscado))
else:
    print('Numero {} no se encuentra en el arbol'.format(NumeroBuscado))

print("\nElimine 3 numeros del arbol")
for i in range(3):
    print('Eliminacion #{}:'.format(i+1))
    NumeroEliminar = int(input())
    eliminar_nodo(Arbol,NumeroEliminar)

print("Numeros pares:",ContadorPares)
print("Numeros impares:",ContadorImpares)
