print("============================================================")
print("              Ejercicio 04 de bucles                        ")
print("============================================================")

contador_negativos=0
contador_positivos=0
introducir=int(input("Ingresa cuantos numeros vas querer introducir"))

for i in range(introducir):
     numeros=int(input(f"Ingresa el valor en la posision {i}"))
     if numeros>=0:
        contador_positivos+=1                  
     if numeros<0:
        contador_negativos+=1
print(f"El total de positivos ingresados es de {contador_positivos}")    
print(f"El total de negativos ingresados es de {contador_negativos}")
