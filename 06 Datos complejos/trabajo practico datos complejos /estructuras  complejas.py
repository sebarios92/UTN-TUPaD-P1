#primer ejercicio
#agregamos una funsion
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#definimos una funsion
def agregar_fruta(diccionario, fruta, precio):
    diccionario[fruta] = precio
#agregamos frutas
agregar_fruta(precios_frutas, 'Naranja', 1200)
agregar_fruta(precios_frutas, 'Manzana', 1500)
agregar_fruta(precios_frutas, 'Pera', 2300)
#mostramos por pantalla
print(precios_frutas)


#segundo ejercicio
#actualizamos lista de precios
#definimos la funcion para actualizar los precios
def actualizar_precio(diccionario, fruta, nuevo_precio):
    if fruta in diccionario:
        diccionario[fruta] = nuevo_precio
#llamamos a la funsion
actualizar_precio(precios_frutas, 'Banana', 1330)
actualizar_precio(precios_frutas, 'Manzana', 1700)
actualizar_precio(precios_frutas, 'Melón', 2800)
#mostramos por pantalla
print("Diccionario actualizado (Ejercicio 2):", precios_frutas)


#tercer ejercicio
#Lista de frutas sin precios
#creamos la funsion lista de frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas (Ejercicio 3):", lista_frutas)


#cuarto ejercicio
#nombramos la planilla
class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
#definimos la funsion
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")#mostramos por pantalla
# Ejemplo
persona1 = Persona("sebastian", "Argentina", 33)
persona1.saludar()


#quinto ejercicio
# Ejercicio 5 - Clase Circulo

import math  #importamos
#nombramos la planilla
class Circulo:
    def __init__(self, radio): #iniciamos con __init__
        self.radio = radio

    def calcular_area(self):  #definimos una funsion
        return math.pi * self.radio ** 2 #retornamos la operacion

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
# Ejemplo 
c1 = Circulo(5)
#mostramos por pantalla
print("Área (Ejercicio 5):", c1.calcular_area()) 
print("Perímetro (Ejercicio 5):", c1.calcular_perimetro())


#sexto ejercicio
#definimos una funsion
def esta_balanceado(expresion):
    pila = [] #llamamos al lifo
    pares = {')': '(', ']': '[', '}': '{'}
#agresegamos un bucle for
    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()
    return not pila
# Ejemplos 
#mostramos por pantalla
print("¿Balanceado? ([{}]) ->", esta_balanceado("([{}])"))  # True
print("¿Balanceado? ([)] ->", esta_balanceado("([)]"))      # False


#septimo ejercicio
#importamos 
from collections import deque
# colocamos un fifo
cola = deque()
#definimos una funsion
def agregar_cliente(nombre):
    cola.append(nombre)
#definimos una funsion
def atender_cliente():
    if cola:
        return cola.popleft()
    return 
#definimos una funsion
def siguiente_cliente():
    if cola:
        return cola[0]
    return 
# Ejemplo
agregar_cliente("Ana")
agregar_cliente("Luis")
#mostramos por pantalla
print("Siguiente cliente:", siguiente_cliente())
print("Atendiendo:", atender_cliente())
print("Siguiente cliente:", siguiente_cliente())


#octavo ejercicio
#nombramos la planilla
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
#nombremos la planilla
class ListaEnlazada:
    def __init__(self): #iniciamos
        self.inicio = None
#definimos una funsion
    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.inicio
        self.inicio = nuevo_nodo
#definimos una funsion
    def mostrar(self):
        actual = self.inicio
        while actual: #iniciamos un bucle while
            print(actual.dato)
            actual = actual.siguiente
# Ejemplo
lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(1)
#mostramos por pantalla
print("Lista enlazada (Ejercicio 8):")
lista.mostrar()


#noveno ejercicio
#definimos una funsion
def invertir_lista(lista):
    anterior = None
    actual = lista.inicio
    while actual: #iniciamos un bucle
        siguiente = actual.siguiente
        actual.siguiente = anterior
        anterior = actual
        actual = siguiente
    lista.inicio = anterior
# Invertimos 
invertir_lista(lista)
#mostramos por pantalla
print("Lista enlazada invertida (Ejercicio 9):")
lista.mostrar()