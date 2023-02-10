'''
Solicitar al usuario una distancia en metros y transformar a km., cm. o mm. 
'''

#Entrada

distancia = int(input("Ingrese la distancia en metros: "))

#Proceso

km = (distancia / 1000)
cm = (distancia * 100)
mm = (distancia * 1000)

#Salida

print(f"{distancia} metros son {km} kilometros")
print(f"{distancia} metros son {cm} centimetros")
print(f"{distancia} metros son {mm} milimetros")