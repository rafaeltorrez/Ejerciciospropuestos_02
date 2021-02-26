import math
print("=========================================================")
print("          Ejercicio 07 de condiciones                    ")
print("=========================================================")

a=int(input("Ingresa el valor del coeficiente A "))
b=int(input("Ingresa el valor del coeficiente B "))
c=int(input("Ingresa el valor del coeficiente C "))

valor3=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)
#valorx1=(-b+(((b**2)-(4*a*c))**0.5))/(2*a)

valorx2=(-b-(((b**2)-(4*a*c))**0.5))/(2*a)

print(f"el valor de x1 es de {valor3}")
print(f"el valor de x2 es de {valorx2}")