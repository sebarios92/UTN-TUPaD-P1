#primer ejercicio
#definimos una funcion
multiplos_de_4 = list(range(4, 100, 4))#realizamos una lista de numeros multiplos
print("rango de numeros multiplos del 4 al 100:    ", multiplos_de_4)#mostramos por pantalla

#segundo ejercicio
#definimos una funcion
lista_de_elementos = ("manzana", "pera", "banana", "kiwi", "frutilla")
penultimo_elemento = (lista_de_elementos)[-2]#pedimos traer el penultimo elemento
print("penultimo elemento de la lista:    ", penultimo_elemento)#mostramos por pantalla


#tercer elementos
lista_vacia = []#creamos una lista vacia
lista_vacia.append(["vaca", "oveja", "conejo"])#agregamos elementos a la lista
print("esta es la nueva lista:   ", lista_vacia)#mostramos en pantalla


#cuarto ejercicio
lista_de_animales = ["perro","gato","conejo","pez"]#creamos una lista de elementos
lista_de_animales[1]= "loro"#cambiamos el indice 1
lista_de_animales[3]= "oso"#cambiamos el indice 3
print("esta es la nueva lista:   ", lista_de_animales)#mostramos por pantalla


#quinto ejercicio
#en este ejercicio usamos la funsion remove y max para eliminar el numero mas alto de la lista 
#luego mostramos en pantalla la lista de numeros ya sin en este caso el numero 22 que seria el del valor mas alto
numeros = [8, 15, 3, 22, 7]#armamos una lista
numeros.remove(max(numeros))#removemos el valor mas alto de la lista
print("esta es la nueva lista de numeros:",   numeros)#mostramos por pantalla


#sexto ejercicio
lista_de_numeros = list(range(10, 30, 5))#creamos una lista con rango
primer_numero_de_la_lista = (lista_de_numeros)[0]#traemos el indice 0
segundo_numero_de_la_lista = (lista_de_numeros)[1]#traemos el indice 1
print("el primer y el segundo numero de la lista es:    ", primer_numero_de_la_lista,"y", segundo_numero_de_la_lista)


#septimo ejercicio
lista_autos = ["sedan", "polo", "suran", "gol"]#creamos una lista
lista_autos[0] = "peugeot"#cambiamos el indice 0 de la lista
lista_autos[1] = "fiat"#cambiamos el indice 1 de la lista
print("la nueva lista de auto es:    ", lista_autos)#mostramos por pantalla


#octavo ejercicio
lista_dobles = []#creamos una lista vacia
lista_dobles.append(5 * 2)#agregamos una multiplicacion
lista_autos.append(10 * 2)#agregamos una multiplicacion
lista_autos.append(15 * 2)#agregamos una multiplicacion
print(lista_dobles)#mostramos por pantalla


#noveno ejercicio
compras = [["pan","leche"], ["arroz","fideos","salsa"],["agua"]]
compras[-1].append("jugo")
compras[-2][1] = "tallarines"
compras[0].remove("pan")
print(compras)


#decimo ejercicio
lista_anidada = [15, True, [25.5, 576.9, 30.6], False]
print(lista_anidada)