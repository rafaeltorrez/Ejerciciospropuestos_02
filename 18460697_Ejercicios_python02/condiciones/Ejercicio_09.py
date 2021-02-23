print("=========================================================")
print("          Ejercicio 09 de condiciones                    ")
print("=========================================================")

res="si"
while res=="si":
      print("Calcular la distancia de centimetros a kilomentros  selecciona las teclas K o k ")
      print("Calcular la distancia de Centimetros a metros selecciona las teclas M o m ")
      print("Salir del programa presiona las teclas si o no")
      print("Selecciona que tipo de distancia deceas calcular ")
      tipo_distancia=input().lower
      if tipo_distancia()=="K" or tipo_distancia()=="k":  
         print("===========================================================")
         print("        Conversion de centimetros a kilometros             ") 
         print("===========================================================") 
         distancia=int(input("Ingresa la distancia en centimetros"))
         total_km=distancia*(1/100)*(1/1000)  
         print(f"la convercion de cm a km es de ",round(total_km,2))
      elif tipo_distancia()=="M" or tipo_distancia()=="m": 
         print("==========================================================")
         print("        Conversion de centimetros a metros                ")
         print("==========================================================")
         distancia=int(input("Ingresa la distancia en centimetros"))                  
         total_metros=distancia/100
         print(f"la conversion de cm a m es de ", round(total_metros,2))              
      elif tipo_distancia()=="no":
         print("Toda via sigues dentro del programa")
      elif tipo_distancia()=="si": 
         print("Has salido del programa correctamente")
         break