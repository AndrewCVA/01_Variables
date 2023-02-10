'''
Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.
'''

#Entrada

num = int(input("Ingrese el número a calcular: "))

#Proceso

total1 = num*30/100
total2 = num*60/100
total3 = num*90/100

#Salida

print(f"Según los datos, el 30% del número es {total1}, el 60% es {total2} y el 90% es {total3}")