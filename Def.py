""""Ejercicio
print("Archivo ejecutado")

def Saludo():
    print("Hola")

Saludo()

def Saludo(Nombre):
    print(f"Hola{Nombre}")
    Saludo("Angel")

def sumar (a,b):
    Resultado = a + b
    return Resultado
sumar(2,3)
print(sumar(2,3)) # guardar la variable en la funcion
numero = sumar(2,3)
print(numero)
numero + 4
print(numero + 4)

def Imprimir_pares_hasta(n):
    for Numero in range(1,n+1):
    if Numero % 2 == 0:
        print(Numero)
Imprimir_pares_hasta(10)

def Solicitar_nombre():
    Nombre = input("Ingrese su nombre: ")
    return Nombre

def Saludar():
    Nombre = Solicitar_nombre()
    print (f"Hola   {Nombre}")
Saludar()    

def Pedir_numeros():
    numero1 = input("Ingrese el primer numero: ")
    numero2 = input ("ingrese el segundo numero: ")
    return numero1, numero2

def Sumar():
    a,b = Pedir_numeros()
    resultado = a + b
    print(f"El resultado es {resultado}")
Sumar()
"""

def solicitar_numero():
    numero = int(input("Ingrese un número entero positivo: "))
    return numero


def calcular_factorial(n):
    factorial = 1
    
    for i in range(1, n + 1):
        factorial *= i   # factorial = factorial * i
        
    return factorial


def mostrar_resultado():
    n = solicitar_numero()
    resultado = calcular_factorial(n)
    print(f"El factorial de {n} es {resultado}")


# Ejecutar programa
mostrar_resultado()
    

