def menu_1():
   print("======================================================")
   print(               "Menu de opciones                       ")
   print("======================================================")
   print("1.Generar nuevo numero de control ")
   print("2.salir del programa")
   menu=int(input("Ingrese que opcion quiere"))
   if menu==1:
      def generar_numero():
         print("=======================================================")
         print("              Generar numeros de control               ")
         print("=======================================================")
         diccionario = dict()
         
         numero_control=int(input("Ingresa el año de ingreso del alumno "))
         campus=int(input("Ingresa el numero del campus del alumno "))
         digito=int(input("Ingresa el ultimo digito ")) 
         
         reg=numero_control+campus+digito
         diccionario={"reg": reg}
         for i in diccionario:
           print(diccionario[i])
      generar_numero()
      menu_1()

menu_1()
