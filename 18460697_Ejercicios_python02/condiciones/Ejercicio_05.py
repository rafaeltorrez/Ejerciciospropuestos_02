print("===========================================")
print("         Ejercicio 05 condiciones          ")
print("===========================================")

numero1=int(input("Ingresa el valor numero 1 "))
numero2=int(input("Ingresa el valor numero 2 "))
numero3=int(input("Ingresa el valor numero 3 "))

if numero1==numero2==numero3:
   print("Los 3 numeros son iguales")
elif numero1==numero2:
    print(f"el numero {numero1} es igual a {numero2}")
elif numero1==numero3:
       print(f"el numero {numero1} es igual a {numero3}")  
elif numero2==numero3:
    print(f"el numero {numero2} es igual a {numero3}")
else:
    print(f"los numeros {numero1}, {numero2}, {numero3} son distintos")