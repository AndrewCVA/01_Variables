'''
Solicitar tiempo en segundos y transformar a horas y minutos. 
'''

#Entrada

segundos = int(input("Ingrese los segundos a calcular: "))

#Proceso

minutos = segundos/60
horas = minutos/60

#Salida

print(f"{segundos}segundo son {minutos} minutos y en horas son {horas}")