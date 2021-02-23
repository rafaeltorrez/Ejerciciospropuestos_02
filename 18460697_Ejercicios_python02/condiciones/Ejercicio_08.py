print("=========================================================")
print("          Ejercicio 08 de condiciones                    ")
print("=========================================================")

res="no"
while res=="no":
     print("Area triangulo presiona las teclas T o t ")
     print("Area circulo presiona las teclas C o c ")
     print("Salir del programa presiona las teclas si / no")
     print("Ingresa que tipo de figura quieres ")
     decision=input().lower
     if decision()=="T" or decision()=="t":
          print("==================================================")
          print("              Area triangulo                      ")
          print("==================================================")
          base=float(input("Ingresa la base del triangulo "))
          altura=float(input("Ingresa la altura del triangulo "))
          area_triangulo=base*altura/2
          print(f"El area del triangulo es de ", round(area_triangulo,2))
     elif decision()=="C" or decision()=="c":
          print("==================================================")
          print("                Area Circulo                      ")
          print("==================================================")
          pi=3.141592
          radio=float(input("Ingresa el radio del circulo"))
          area_circulo=pi*radio**2
          print(f"El area del circulo es de ", round(area_circulo,2))
     elif decision()=="si":
          print("Ha salido del programa correctamente")
          break
     elif decision()=="no":
          print("Sigues dentro del programa")
 


     




