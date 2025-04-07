#primer programa
#pedimos al usuario que ingrese su edad
edad = int(input("ingrese su edad:  "))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")


#segundo programa
#pudimos al usuario que ingrese su nota
nota = float(input("ingrese su nota:  "))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")


#tercer progrma
#pedimo al usuario que ingrese un numero par
numero = int(input("ingrese un numero par:  "))
#cualculamos si divir por 2 el resto da cero
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")


#cuarto programa
#pedimos al usuario que ingrese su edad
edad = int(input("ingrese su edad:  "))
#clasificamos las edades y mostramos en pantalla
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad <= 18:
    print("adolecente")
elif edad >= 18 and edad <= 30:
    print("adulto/a joven")
else:
    print("adulto/a")


#quinto programa
def verificar_contraseña(contraseña):
#calculamos la longitud de la contrasena
    longitud = len(contraseña)
    if 8 <= longitud <= 14:
        print("ha ingresado una contraseña correcta")
    else:
        print("por favor ingrese una contraseña que contenga entre 8 y 14 caracteres")
#solicitamos al usuario que ingrese una contrasena
contraseña = input("ingrese una contraseña de 8 a 14 caracteres: ")
#llammos a la funcion para verificar contrasena
verificar_contraseña(contraseña)


#sexto programa
import random
from statistics import mode, median, mean
#calculamos la moda, la mediana y la median
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda_calculada = mode(numeros_aleatorios)
mediana_calculada = median(numeros_aleatorios)
media_calculada = mean(numeros_aleatorios)
#determinamos el sesgo de la distribucion de los numeros aleatorios
if media_calculada > mediana_calculada > moda_calculada:
    print("Sesgo positivo o a la derecha")
elif media_calculada < mediana_calculada < moda_calculada:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")
#imprimimos los resultados
print("Moda:", moda_calculada)
print("Mediana:", mediana_calculada)
print("Media:", media_calculada)


#septimo progrma
#definimos una cadena con las vovales (MAYUSCULAS y minusculas)
def agregar_signo_exclamacion_si_vocal(texto):
    vocales = "aeiouAEIOU"
#verificamos si el texto no esta vacio
    if texto and texto[-1] in vocales:
        return texto + "!"
    else:
        return texto
#mostramos los resultados en pantalla
texto_ingresado = input("Ingrese una frase o palabra: ")
texto_modificado = agregar_signo_exclamacion_si_vocal(texto_ingresado)
print(texto_modificado)


#octavo programa
#transformamos el texto a upper, lower, title
def transformar_nombre(nombre, numero):
    if numero == 1:
        return nombre.upper()
    elif numero == 2:
        return nombre.lower()
    elif numero == 3:
        return nombre.title()
    else:
        return "opcion invalida"
#pedimos al usuario que ingrese su nombre
nombre_ingresado = input("Ingrese su nombre: ")
opcion_ingresada = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para título: "))
#llamamos a las funsiones para transformar el texto ingresado
nombre_transformado = transformar_nombre(nombre_ingresado, opcion_ingresada)
#imprimimos en pantalla el resultado
print(nombre_transformado)


#noveno programa
#pedimos al usuario que ingrese un numero en la escala de richter
escala_de_richter = int(input("ingrese el numero del terremoto segunb las escala de richter:  "))
#clasificamos las escalas 
if escala_de_richter < 3:
    print("muy leve (imperceptible)")
elif escala_de_richter >= 3 and escala_de_richter <4:
    print("leve (ligereamente perceptible)")
elif escala_de_richter >= 4 and escala_de_richter <5:
    print("moderado (sentido por personas, pero generalmente no causa daños)")
elif escala_de_richter >= 5 and escala_de_richter <6:
    print("fuerte (puede causar daños en estructuras debiles)")
elif escala_de_richter >= 6 and escala_de_richter <7:
    print("muy fuerte (puede causar daños significativos)")
elif escala_de_richter >= 7:
#imprimos en pantalla los resultados
    print("extremo (puede causar graves daños a gran escala)")
else:
    print("ingrese un numero de la escala de richter")

#decimo programa
#definimos los meses
meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}

def obtener_estacion(dia, mes, hemisferio):
#determinamos las estaciones segun mes y hemisferio
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
#devolvemos la estacion correspondiente
    return estacion_norte if hemisferio.upper() == 'N' else estacion_sur
#solicitamos al usuario que ingrese los datos
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip()
mes_nombre = input("¿Qué mes es? (ej: marzo): ").strip().lower()
dia = int(input("¿Qué día es? (1-31): "))
#verificamos si el mes ingresado es valido
if mes_nombre in meses:
    mes = meses[mes_nombre]
    estacion = obtener_estacion(dia, mes, hemisferio)
    print(f"Estás en {estacion}.")
else:
    print("Mes no válido. Por favor, escribilo correctamente (ej: enero, febrero, etc.).")