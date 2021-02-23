print("============================================================")
print("              Ejercicio 01 de bucles                        ")
print("============================================================")

lista_numeros=[]
cantidad=6
lista_pares=[]
lista_impares=[]

def capturar_numeros():
      for i in range(cantidad):
          numeros=int(input("Ingresa los valores ala lista "))
          lista_numeros.append(numeros)

def mostrar_lista(lista_numeros):
     contador_par=0
     contador_impar=0
     suma_par=0
     suma_impar=0
     for i in range(len(lista_numeros)):
        if lista_numeros[i]%2==0:
            lista_pares.append(lista_numeros[i])
        else:
            lista_impares.append(lista_numeros[i])
     print("Pares")
     for i in lista_pares:
        suma_par=suma_par+i
     print(lista_pares, "La suma es de los numeros pares es ", suma_par)

     print("_________________________________")
     print("No pares")
     for i in lista_impares:
        suma_impar=suma_impar+i
     print(lista_impares, "La suma es de los numeros impares es ", suma_impar)

     for i in lista_pares:
          if lista_pares[i]%lista_pares==0:
             print("es primo")           
capturar_numeros()
mostrar_lista(lista_numeros)
