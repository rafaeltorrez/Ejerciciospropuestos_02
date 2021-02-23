print("===========================================")
print("         Ejercicio 04 condiciones          ")
print("===========================================")

multiplo=0
numero1=int(input("Ingresa el valor numero 1 "))
numero2=int(input("Ingresa el valor numero 2 "))
if numero1>numero2:
     multiplo=numero1%numero2
     if multiplo==0:
         print(f"el numero {numero1} es multiplo de {numero2}")
     else:
         print(f"el numero {numero1} No es multiplo de {numero2}")
elif numero2>numero1:
     multiplo=numero2%numero1
     if multiplo==0:
        print(f"el numero {numero2} es multiplo de {numero1}")
     else:
        print(f"el numero {numero2} No es multiplo de {numero1}")
elif numero1==numero2:
     print(f"el numero {numero1} es igual a {numero2}")
    