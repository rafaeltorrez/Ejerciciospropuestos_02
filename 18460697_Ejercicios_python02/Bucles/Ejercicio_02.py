print("============================================================")
print("              Ejercicio 02 de bucles                        ")
print("============================================================")

res="si"
while res=="si":
    numero=int(input("Ingrese el numero para calcular sus divisores"))
    for i in range(1,numero+1): 
      if numero%i==0:
          print(i)
    print("Deseasa volver a ingresar otro numero si o no ") 
    respuesta=input().lower
    if respuesta()=="si": 
       print("Has salido del programa ")
       break 
    elif respuesta()=="no":
       print("No has salido del programa toda via")