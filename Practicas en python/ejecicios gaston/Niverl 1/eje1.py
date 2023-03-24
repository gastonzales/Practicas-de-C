##Pedir 2 n�meros al usuario y sumarlos, restarlos, multiplicarlos 
## y dividirlos
 
# I'm going to start solving the problem 


# I wil var

var1=0
var2=0
restult=0

def operacion (num1, num2):
	suma= num1 + num2
	resta=  num1 - num2
	mult= num1*num2
	div= num1/ num2
	return suma, resta, mult, div


print("Suma: Ingrese los numeros que se sumaran")
var1= int(input()) 
var2= int(input("Ingrese otro valor: \n"))

su, re, mu, di=operacion(var1, var2)

opcion= int (input("""Elija opracion a realizar
	1. Suma.
	2. Resta
	0. Salir\n"""))

if(opcion==1):
	print(su)

