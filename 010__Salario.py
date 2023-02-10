'''
Programa que permita determinar el 
salario a pagar a un empleado, teniendo 
como entradas el salario diario y el 
número de días trabajados. Tenga en 
cuenta que al empleado se le debe 
descontar el 10% por concepto de 
pensión y 15% por concepto de salud.
'''

#Entrada

salariodiario = float(input("Ingresar el salario diario: "))
dias = int(input("Ingresar los dias trabajados: "))


#Proceso

salariototal = salariodiario*dias
pension = salariototal*0.10
salud = salariototal*0.15
pagafinal = salariototal-pension-salud

#Salida

print(f"El salario final que recibe el empleado es de: {pagafinal}")