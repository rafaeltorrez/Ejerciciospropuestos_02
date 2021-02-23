print("============================================================")
print("              Ejercicio 03 de bucles                        ")
print("============================================================")

cantidad=int(input("Ingresa cuantos numeros vas ingresar"))
if cantidad<1:
    print("Debes ingresar numeros positivos")
else:
   primero=int(input("Ingresa el valor"))
   for i in range(cantidad-1):
      numero=int(input(f"ingresa otro valor mayor que {primero}")
      if numero<=primero:
         print(f"el numero {numero} no es mayor que {primero}")    
