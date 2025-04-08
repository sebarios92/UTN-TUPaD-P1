#primer ejercicio
for numero in range(101): #usamos range para incluir el 100
    print(numero)


#segundo ejercicio
def contar_digitos(numero):
    # Manejar el caso especial de 0
    if numero == 0:
        return 1
    # Convertir el número a su valor absoluto 
    numero = abs(numero)
    # usamos el contador +
    contador = 0
    # Contar 
    while numero > 0:
        numero //= 10  # Dividir el número por 10 (división entera)
        contador += 1
    return contador

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))
# usamos el contador 
cantidad_digitos = contar_digitos(numero)
# Imprimimos el resultado
print(f"El número {numero} tiene {cantidad_digitos} dígitos.")


#tercer ejercicio
def sumar_enteros_entre(valor1, valor2):
    # Asegunos aseguramos que valor1 sea menor que valor2
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1  # Intercambiamos los valores
    #  suma
    suma = 0
    # Sumamos los números enteros entre valor1 y valor2
    for numero in range(valor1 + 1, valor2):
        suma += numero
    return suma
# Solicitamos que ingrese los dos valores enteros
valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))
# Calcular la suma
suma_total = sumar_enteros_entre(valor1, valor2)
# mostramos por pantalla
print(f"La suma de los números enteros entre {valor1} y {valor2} es: {suma_total}")


#cuarto ejercicio
def sumar_enteros_hasta_cero():
    suma_total = 0  # Iniciamos la suma en 0
    numero = int(input("Ingresa un número entero (0 para terminar): "))  # Pedimos el primer número
    while numero != 0:  # Mientras el número no sea 0
        suma_total += numero  # Sumar el número a la suma total
        numero = int(input("Ingresa otro número entero (0 para terminar): "))  # Pedimos el siguiente número
    return suma_total
# Llamamos a la funsion
suma = sumar_enteros_hasta_cero()
print(f"La suma total de los números ingresados es: {suma}") #imprimimos en pantalla



#quinto ejercicio
import random
def adivina_el_numero():
    numero_secreto = random.randint(0, 9)  # Generamos un número aleatorio entre 0 y 9
    intentos = 0  # Iniciamos el contador de intentos

    print("¡Adivina el número secreto! (entre 0 y 9)")

    while True:
        intento = int(input("Ingresa tu intento: "))  # pedimos al usuario que ingrese un número
        intentos += 1 
        if intento == numero_secreto:  
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break  #salimos
        elif intento < numero_secreto:  
            print("El número secreto es mayor.")
        else:  
            print("El número secreto es menor.")

# Iniciar el juego
adivina_el_numero()



#sexto ejercicio
def imprimir_pares_decreciente():
    for numero in range(100, -1, -2): #inicia en 100, termina en 0, va de 2 en 2 en orden decreciente
        print(numero)
#imprimimos
imprimir_pares_decreciente()


#septimo ejercicio
def suma_enteros_hasta_n(n):
    suma = 0 # iniciamos la suma
    for numero in range(n + 1): 
        suma += numero 
    return suma
# pedimos al usuario que ingrese un numero 
numero = int(input("Ingresa un número entero positivo: "))
# Verificar si el número es positivo
if numero < 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    # Calcular la suma
    suma_total = suma_enteros_hasta_n(numero)
    # Imprimimos 
    print(f"La suma de los números enteros desde 0 hasta {numero} es: {suma_total}")


#octavo ejercicio
def analizar_numeros(numeros):#analizamos una lista de numeros
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    return {
        "pares": pares,
        "impares": impares,
        "positivos": positivos,
        "negativos": negativos,
    }
numeros_ingresados = []
cantidad_numeros = 100  # Cambiar a un número menor para pruebas
for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    numeros_ingresados.append(numero)
# Analizar los números ingresados
resultados = analizar_numeros(numeros_ingresados)
# Imprimimos en pantalla los resultados
print(f"Cantidad de números pares: {resultados['pares']}")
print(f"Cantidad de números impares: {resultados['impares']}")
print(f"Cantidad de números positivos: {resultados['positivos']}")
print(f"Cantidad de números negativos: {resultados['negativos']}")


#noveno ejercicio
def calcular_media(numeros):
    if not numeros: #Si la lista esta vacía
        return 0
    suma = sum(numeros) #suma 
    media = suma / len(numeros) #dividimos
    return media
numeros_ingresados = []
cantidad_numeros = 100 

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    numeros_ingresados.append(numero)
# Calculamos la media de los números ingresados
media_total = calcular_media(numeros_ingresados)

# Imprimimos el resultado por pantalla
print(f"La media de los números ingresados es: {media_total}")



#decimo ejercicio
def invertir_digitos(numero):
    numero_str = str(abs(numero))  # Convertir el número a una cadena
    numero_invertido_str = numero_str[::-1]  # Invertimos la cadena
    if numero < 0:
        numero_invertido = -int(numero_invertido_str)
    else:
        numero_invertido = int(numero_invertido_str)
    return numero_invertido
# Solicitamos al usuario que ingrese un numero entero
numero = int(input("Ingresa un número entero: "))
# Invertimos los número
numero_invertido = invertir_digitos(numero)

# Imprimimos en pantalla el resultado
print(f"El número con los dígitos invertidos es: {numero_invertido}")

