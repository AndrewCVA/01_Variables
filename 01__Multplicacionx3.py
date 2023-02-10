'''
Programa que permita multiplicar 3 números.
'''

#Entrada

print("Inserte un Número del 1 al 9")

num1 = int(input("Ingresar primer número: ")) 
num2 = int(input("Ingresar segundo número: "))
num3 = int(input("Ingresar tercer número: "))

#Proceso

total = num1*num2*num3

#Salida

if num1 >0 and num1 <=9 and num2 >0 and num2 <=9 and num3 >0 and num3 <=9:
    print (f"El total es: {total}")
else:
    print("Algun Número es inválido, porfavor intente denuevo.")


