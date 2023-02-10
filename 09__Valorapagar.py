'''
Programa que permita a una tienda saber
el valor que pagara un cliente por la 
compra de varios elementos de la misma
referencia. Debe tener como entradas el 
valor unitario, la cantidad de productos 
comprados y al valor final se debe 
adicionar el 16% correspondiente al IVA.
'''

#Entrada

valorunit = int(input("Ingresar el vaalor unitario del producto: "))
cantidad = int(input("Ingresar cantidad de productos: "))


#Proceso

total = valorunit*cantidad
iva = total*0.16
vfinal = total-iva

#Salida

print(f"El valor a pagar es de {vfinal}")

