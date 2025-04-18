#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.


for i in range(0,101): 
    print (i)
    i+=1





##2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.


num = int (input("Ingrese un número entero"))

if num >0: 

    texto = str(num)

    digitos = len (texto)

    print (f"La cantidad de digitos es {digitos}")
else :
    texto = str(num)

    digitos = len (texto) - 1
    print (f"La cantidad de digitos es {digitos}")

    #3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.


num1 = int(input("Ingrese el primer número entero"))

num2 = int(input("Ingrese el segundo número entero"))

suma = 0
for i in range ((num1 +1 ), num2):

    suma +=  i


print(f"La suma es {suma}")

    
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0




num1 = int(input("Ingrese el primer número entero"))

suma = 0 

while num1 != 0 :
    suma = num1 + suma
    num1 = int(input("Ingrese el primer número entero"))

print (f"La suma acumulada es {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random
adivinar = random.randint(0,9)



intentosAcumulados = 1
adivinado = False
intento = int (input("Ingrese un número del 0 al 9"))
while  intento != adivinar:
    
    intentosAcumulados += 1
    intento= int (input("Ingrese un número del 0 al 9"))

if intento == adivinar:
    adivinado = True
    print(f"Adivinaste el número en {intentosAcumulados}, intentos.")
else:
        print("Incorrecto. Intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente

i= 100
for i in range (100, -1, -2):
    print (i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.





num = int(input("Ingrese un número"))

suma = 0 

for i in range (0, num +1 ):
    suma = i + suma
   

print (f"La suma acumulada es {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio)


pares = 0
impares = 0
positivos = 0
negativos = 0

num = 100

for i in range(num):
    numero = int(input(f"Ingresa el número {i + 1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Números pares:", pares)
print("Números impares:", impares)
print("Números positivos:", positivos)
print("Números negativos:", negativos)


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).


num = 100

suma = 0

for i in range(num):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    suma = numero + suma


media = suma / num

print(f"La media es {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.



num = int (input("Ingrese un numero"))



if num > 0 :
    texto = str (num)[::-1]
    numeroInvertido = int (texto)

else:

    numeroAbsoluto = abs(num)

    texto = str (numeroAbsoluto)[::-1]
    numeroInvertido = -int (texto)


print (numeroInvertido)

