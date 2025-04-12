#primer ejercicio
#definimos la funcion
def imprimir_hola_mundo():
    print("hola mundo")#imprimimos en pantalla

#progrma principal
imprimir_hola_mundo()#llamamos a la funsion


#segundo ejercicio
#definimos la funsion
def saludar_usuario(nombre):
    return f"hola {nombre}"
#programa principal
nombre_usuario = input("ingrese su nombre:   ")#pedimos al usuario que ingrese su nombre
saludo = saludar_usuario(nombre_usuario) #llamamos a la funsion
print(saludo) #imprimimos en pantalla


#tercer ejercicio
def informacion_personal(nombre, apellido, edad, residencia): #definimos la funsion
    return f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
#progrma principal
#pedimos informacion al usuario
nombre_de_usuario = input("ingrese su nombre:   ")
apellido_de_usuario = input("ingrese su apellido:  ")
edad_de_usuario = int(input("ingrese su edad:  "))
residencia_de_usuario = input("ingrese su residencia:  ")
#llamamos a la funcion
informacion = informacion_personal(nombre_de_usuario, apellido_de_usuario, edad_de_usuario, residencia_de_usuario)
print(informacion)#mostramos por pantalla


#cuarto programa
import math #importamos modulo
#definimos la funsion
def calcular_area_del_circulo(circulo):
    area = math.pi * radio ** 2
    return area 
def calcular_perimetro_circulo(radio):#definimos la funsion
    perimetro = 2 * math.pi * radio
    return perimetro
#programa principal
#pedimos al usuario que ingrese el radio
radio = float(input("ingrese el radio del circulo:  "))
#calculamos el area
area = calcular_area_del_circulo(radio)# llamamos a la funsion
perimetro = calcular_perimetro_circulo(radio)#llamamos a la funcion
print(f"el area del circulo es:  {area: .2f}")#mostramos en pantalla
print(f"el perimetro del erea es: {perimetro: .2f}")#mostramos en pantalla


#quinto ejercicio
def segundos_a_horas(segundos):#definimos las funsiones
    horas = segundos / 3600 
    return horas # devolvemos los segundos en horas
#programa principal
#pedimos al usuario que ingrese los segundos
segundos = int(input("ingrese los segundos:  "))
#llamamos a la funsion
horas = segundos_a_horas(segundos)
#imprimimos en pantalla
print(f"{segundos} equivalen a {horas: .2f} horas" )


#sexto ejercicio
#definimos las funsiones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i #calculamos
        print(f"{numero} x {i} = {resultado}")
#programa principal
numero = int(input("ingrese un numero:  "))#pedimos al usuario que ingrese un numero
tabla_multiplicar(numero)#llamamos a la funsion


#septimo ejercicio
#definimos las funsiones 
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division
num1 = int(input("ingrese el primer numero:  "))
num2 = int(input("ingrese el segundo numero:  "))
resultado = operaciones_basicas(num1, num2)
print(f"los resultados de las operaciones con {num1} y {num2}:")

print(f"  suma: {resultado[0]:.2f}")
print(f"  resta: {resultado[1]: .2f}")
print(f"  multiplicacion: {resultado[2]: .2f}")
print(f"  division: {resultado[3]: .2f}")



#octavo ejercicio
#definimos las funsiones
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
#pedimos al usuario que ingrese unos datos
peso = float(input("ingrese su peso:   "))
altura = float(input("ingrese su altura:   "))
imc_resultado = calcular_imc(peso , altura)#llamamos a la funsion
print(f" su indice de masa corporal es: {imc_resultado: .2f}")#mostramos en pantalla


#noveno ejercicio
#definimos las funsiones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit
#programa principal
#pedimos al usuario que ingrese los celsius
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)#llamamos a a la funsion
# Mostramos por pantalla
print(f"{celsius} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")



#decimo ejercicio
#definimos las funsiones
def calcular_promedio(a, b, c):
    promedio =  (a + b + c) / 3 #realizamos la suma
    return promedio
#programa principal
#pedimos al usuario que ingrese los numeros
numero1 = int(input("ingrese el primer numero:  "))
numero2 = int(input("ingrese el segundo numero:  "))
numero3 = int(input("ingrese el tercer numero:  "))
#llamamos a la funsion
promedio = calcular_promedio(numero1, numero2, numero3)
print(f"el promedio de los numeros ingresado es: {promedio: .2f}")#imprimos por pantalla