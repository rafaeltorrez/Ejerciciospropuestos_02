print("============================================================")
print("              Ejercicio 05 de bucles                        ")
print("============================================================")

mayor=0
menor=0
suma=0 
media_aritmetica=0
lista_numeros=[]
cantidad=int(input("Cuantos numeros quieres ingresar "))
for i in range(cantidad):
     numeros=int(input(f"ingresa el valor {i}"))
     suma=suma+numeros
     media_aritmetica=suma/cantidad
     lista_numeros.append(numeros) 
     
mayor=max(lista_numeros)
menor=min(lista_numeros)
print(lista_numeros)
print(f"El mayor es {mayor}")
print(f"El menor es {menor}")
print(f"La suma es {suma}")
print(f"La media aritmetica es de {media_aritmetica}")