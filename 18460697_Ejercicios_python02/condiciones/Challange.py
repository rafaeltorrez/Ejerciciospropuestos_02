def fecha_dia():
      dia=int(input("Ingrese el dia "))
      if dia>0 and dia>31:
        print(f"Error solo hay 31 dias ingresa numeros menores a 31")
        fecha_dia()
      mes=int(input("Ingresa el mes "))
      if mes>=1 and mes>12:
        print(f"Error solo hay 12 meses del año")
        fecha_dia()
      ano=int(input("Ingresa el año"))
      if ano<1582:
        print(f"Error debes ingresar un año mayor que 1582 ")
        fecha_dia()
      else:
        suma=0
        #1. A es el cociente de la division de 14 menos el mes entre 12
        a=(14-mes)//12
        #print(f"el cociente es {a}")
        #2. B es año menos A
        b=ano-a
        #print(f"{b}")
        #3. C es mes mas doce veces A menos 2
        c=(mes+12**a)-2
        #print(f"{c}")
        #4. D es el cociente de la division de B entre 4, # 5. E es el cociente de la división de B entre 100
        #6. F es el cociente de la división de B entre 400, 7. G es el cociente de 31 veces C entre 12
        d=(b/4)-(b//100)+(b//400)+((31*c)//12)%7
        if d==0:
          diasemana="Domingo"
        elif d==1:
          diaSemana = "Lunes"
        elif d == 2:
          diaSemana = "Martes"
        elif d == 3:
          diaSemana = "Miercoles"
        elif d == 4:
          diaSemana = "Jueves"
        elif d == 5:
          diaSemana = "Viernes"
        else:
          diaSemana = "Sabado"
        print(f"el dia %d del mes %d del año %d es %s " %(a,b,c,diaSemana)) 
fecha_dia()