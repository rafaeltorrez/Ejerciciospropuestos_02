print("=========================================================")
print("          Ejercicio 06 de condiciones                    ")
print("=========================================================")

a=int(input("Ingresa el valor al coeficiente A "))
b=int(input("Ingresa el valor al coeficiente B "))

if a ==0 and b==0:
     print("Todos los numeros que se capturen son soluciones")
elif a==0:
     print("Tiene una unica solucion")
else:
     x=-b/a
     print(f"La solucion de la ecuacion de 1 grado es de {x}")