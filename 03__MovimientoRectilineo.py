'''
Programa para calcular la distancia
recorrida en un movimiento rectilíneo.
Recuerde x=v*t donde v es
velocidad y t es tiempo. Solicitar al
usuario velocidad en kilómetros por hora 
(Km/h) y tiempo en horas (h) para 
obtener la distancia en kilómetros (Km).
'''

#Entrada

Velocidad = int(input("Ingrese la velocidad en (Km/h): ")) 
Tiempo = int (input("Ingrese el tiempo en (h): "))

#Proceso

Km = Velocidad*Tiempo

#Salida

print(f"La distancia recorrida es de {Km}(Km)")