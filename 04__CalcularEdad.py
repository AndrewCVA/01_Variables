'''
Programa que permita calcular la edad
de una persona conociendo el año actual
y el usuario digita su año de nacimiento.
'''

#Entrada

AñoActual = 2023 
Año = int(input("Ingresar su año de nacimiento: "))

#Proceso 

Edad = AñoActual - Año 

#Salida

if Año >=2023 and Año <=0:
    print("Ese no puede ser tu año de nacimiento.")
else:
    print(f"Tu edad es de {Edad} años aproximadamente")