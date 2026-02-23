def genrar_tablas(numero,limite):
    for n in range  (1,limite+1):
        print(f"{numero} x {n} = {numero*n}")

def Inicio():
    while True:
        print ("\nGenerador de tablas\n")
        num = int (input("ingrese el numero que desea multiplicar:"))
        lim = int(input("ingrese la cantidad de veces que desea multiplicarlo: ")) 
        genrar_tablas(num,lim)

        otra = input("Desea continuar?(s/n)")
        if otra.lower()  != "s":
            break
Inicio()