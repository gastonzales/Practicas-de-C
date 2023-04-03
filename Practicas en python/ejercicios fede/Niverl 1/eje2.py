# 1. Suma de los n primeros n�meros

cantidad_de_numero=int(input("ingrese cantidad de numero a sumar:"))

i=0
total=0
while(cantidad_de_numero > i ):
    num=int(input("ingrese numero:\n"))
    total+=num
    i+=1

print(f"El resultado: {total}")

    
