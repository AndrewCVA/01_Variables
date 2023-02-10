'''
Calcular la hipotenusa con el Teorema de Pitágoras.
'''

#Entrada
 
a = int(input("Ingrese el Catetto Opuesto: "))
b = int(input("Ingrese el Catetto Adyacente: "))

#Proceso

hipotenusa = (a**2 + b**2)
Raiz = hipotenusa**(1/2)
Mdh = round(Raiz)
 
#Salida

print(f"La medida de la hipotenusa es {Raiz}")
print(f"La raiz de la medida de la hipotenusa es {Mdh}")