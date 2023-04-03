#2. Digite un numero, si el numero supera a 10, multiplique los 10 primeros n�meros, 
#sino, sumelos (Propuesto)

cantidad_de_numero=int(input("ingrese cantidad de numeros:"))

i=0
total=1
if (cantidad_de_numero>10):
    while(cantidad_de_numero > i ):
        i+=1
        total*=i
else :
    while(cantidad_de_numero > i ):
        i+=1
        total+=i
    
print(f"El resultado: {total}")

