#Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario
#
def factorial_recursivo(n):
    
    #Calcula el factorial de un número entero no negativo de forma recursiva.
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def calcular_factorial_n():
    
    #Solicita un número al usuario y muestra el factorial de todos los números
  
    while True:
        try:
            numero_usuario = int(input("Ingrese un número entero positivo: "))
            if numero_usuario < 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                break
        except ValueError:
            print("Error. Por favor, ingrese un número entero.")

    print(f"\nCalculando el factorial de los números del 1 al {numero_usuario}:")
    for i in range(1, numero_usuario + 1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

# se llama a la función 

calcular_factorial_n()


#2- Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique


def fibonacci_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def mostrar_serie_fibonacci():
    posicion = input("Ingrese hasta qué posición desea ver la serie de Fibonacci: ")
    
    while not (posicion.isdigit() and int(posicion) >= 0):
        print("Por favor, ingrese un número entero positivo")
        posicion = input("Ingrese hasta qué posición desea ver la serie de Fibonacci: ")
    
    posicion = int(posicion)
    print(f"\nSerie de Fibonacci hasta la posición {posicion}:")

    for i in range(posicion + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")


mostrar_serie_fibonacci()

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula  Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente)

def ejecutar_potencia():
    base = input("Ingrese la base ")
    while not base.replace(".", "", 1).isdigit():
        print("Error. Ingrese un número válido.")
        base = input("Ingrese la base ")
    
    exponente = input("Ingrese el exponente entero")
    while not (exponente.isdigit()):
        print("Error. Ingrese un número entero")
        exponente = input("Ingrese el exponente entero")
    
    base = (base)
    exponente = (exponente)
    resultado = potencia_recursiva(base, exponente)
    
    print(f"\n{base} elevado al {exponente} da como resultado: {resultado}")

#Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto


def convertir_a_binario(n):
    if n == 0:
        return ""
    else:
        return convertir_a_binario(n // 2) + str(n % 2)

def ejecutar_conv():
    numero = input("Ingrese un número entero positivo: ")

    while not (numero.isdigit() and int(numero) > 0):
        print("Error. Ingrese un número entero positivo.")
        numero = input("Ingrese un número entero positivo: ")

    numero = int(numero)
    binario = convertir_a_binario(numero)
    print(f"El número {numero} en binario es: {binario}")


#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es.
 #Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed().



def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


def verificar():
    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")


verificar()


#6 scribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.
#Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
#suma_digitos(9) → 9
#suma_digitos(305) → 8 (3 + 0 + 5

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)



def ejecutar_suma():
    numero = input("Ingrese un número entero positivo: ")

    while not (numero.isdigit() and int(numero) > 0):
        print("Ingrese un número entero positivo.")
        numero = input("Ingrese un número entero positivo: ")

    numero = int(numero)
    resultado = suma_digitos(numero)

    print(f"La suma de los dígitos de {numero} es: {resultado}")

ejecutar_suma()


    #7- Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque


def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
def ejecutar_conteo():
    nivel = input("Ingrese cuántos bloques hay en el nivel más bajo de la pirámide: ")

    while not (nivel.isdigit() and int(nivel) > 0):
        print("Por favor, ingrese un número entero positivo.")
        nivel = input("Ingrese cuántos bloques hay en el nivel más bajo de la pirámide: ")

    nivel = int(nivel)
    total = contar_bloques(nivel)
    print(f"Se necesitan {total} bloques para construir la pirámide completa.")


ejecutar_conteo()

# 8 scribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero / 10, digito)
    else:
        return contar_digito(numero / 10, digito)

def ejecutar_contador():
    numero = input("Ingrese un númeropositivo: ")
    while not (numero.isdigit() and int(numero) > 0):
        print("Por favor, ingrese un número")
        numero = input("Ingrese un número positivo: ")

    digito = input("Ingrese un dígito entre 0 y 9: ")
    while not (digito.isdigit() and 0 <= int(digito) <= 9):
        print("Por favor, ingrese un número de 0 a 9")
        digito = input("Ingrese un número entre 0 y 9: ")

    numero = int(numero)
    digito = int(digito)
    resultado = contar_digito(numero, digito)

    print(f"El dígito {digito} aparece {resultado} veces en el número {numero}.")
    

ejecutar_contador()