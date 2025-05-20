#PRIMER EJERCICIO

def factorial(n):
    if n== 0 or n == 1: #caso base
         #caso recursivo
        return n* factorial(n - 1)
numero = int(input("ingresa un numero entero positivo:   "))#pedimos al usuario que ingrese un numero
#verificamos que sea positivo
if numero< 1:
    print("el numero debe ser mayor o igual a 1")#imprimimos por pantalla
else:
    print(f"factoriales del 1 al {numero}:  ")#de lo contrario 
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial}")#mostramos por pantalla el factorial

#segundo ejercicio

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario una posición
posicion = int(input("Ingresá la posición hasta la cual querés ver la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")


#tercer ejercicio
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Probamos la función con valores ingresados por el usuario
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente (entero no negativo): "))

print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")

#cuarto ejercicio
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Pedimos al usuario un número decimal
numero_decimal = int(input("Ingresá un número entero positivo para convertir a binario: "))

if numero_decimal == 0:
    print("El binario de 0 es: 0")
else:
    binario = decimal_a_binario(numero_decimal)
    print(f"El número {numero_decimal} en binario es: {binario}")#imprimos por pantalla

#quinto ejercicio
def es_palindromo(palabra):#definimos una funsion
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# pedimos al usuario que ingrese una palabra
palabra = input("Ingresá una palabra (sin espacios ni tildes): ").lower()
print(f"¿'{palabra}' es palíndromo?: {es_palindromo(palabra)}")

#sexto ejercicio
def suma_digitos(n):#definimos una funsion
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

#pedimos al usurio que ingrese un numero
numero = int(input("Ingresá un número entero positivo: "))
print(f"Suma de los dígitos de {numero}: {suma_digitos(numero)}")#mostramos por pantalla

#septimo ejercicio
def contar_bloques(n):#definimos una funsion
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# consultamos al usuario
nivel_inferior = int(input("¿Cuántos bloques hay en el nivel más bajo?: "))
print(f"Total de bloques necesarios: {contar_bloques(nivel_inferior)}")#mostramos por pantalla

#octavo ejercicio
def contar_digito(numero, digito):#definimos una funsion
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

# pedimos al usuario que ingrese un numero
numero = int(input("Ingresá un número entero positivo: "))
digito = int(input("¿Qué dígito querés contar (0-9)?: "))
#mostramos por pantalla
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")