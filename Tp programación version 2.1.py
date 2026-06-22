# -*- coding: utf-8 -*-
"""
ECUACIÓN PARENTESIS
"""
#LOTE DE PRUEBA:
A="20(1x+3)+34(1x+2)/2+25x+30x+50+60=50*20"
B="20x+3x+60/20=50*-20"
C="20(1x+3)+34(1x/5+2*3)/4+25x+30x+50+60=50*20"

D="20(1x+3)+30(2x+3)+25(-1x+20)+37+50*27"
E="(x+1)/7=3"

P1="-x+2+2x+3=6"
P2="3x/4+x=1/2-x/2"
P3="(3x-2)-2x+34(4x+2)-4=-1-2x-2"



import copy 
import re
Cantidad_Decimales=2
def Cargar_Lista1(E):
    """
    Está al igual que la anterior función toma una ecuación y la transforma en un lista que contiene tuplas que representan terminos con x y  sin x de la forma (coeficiente, "x") o (coeficiente,"") 
    respectivamente y listas que representan multiplicaciones o divisiones estas listas son de la forma [coeficiente, "*", coeficiente] o [coeficiente,"/", coeficiente] 
    el primer  coeficiente puede ser una tupla si representa un término con x o un float si representa un término sin x. A esto se agregan los parentesis estos son listas que pueden contener tuplasy listas que representan terminos con x y sin x o multiplicaciones o divisiones.

    Parametros
    ----------
    E : string
        Es la ecuación que se quiere transformar en una lista.

    Returns
    -------
    ListaTerminos : list
        DESCRIPTION.
    """
    ListaTerminos=[]
    Numero = str()
    Terna=[]
    Mul_Div=0
    for np,i in enumerate(E):
        if i.isdigit() == True or i == '.':
            Numero = Numero+i
            
        elif i == "x":
            if Numero==str(): 
               Duplas=(1,"x")
               ListaTerminos.append(Duplas)
            elif Numero=="-":
                 Duplas=(-1,"x")
                 Numero=str()
                 ListaTerminos.append(Duplas)
            else:
                 Duplas=(float(Numero),"x") 
                 ListaTerminos.append(Duplas)
                 Numero=str()
            
        elif i=="*" or i=="/":
            if E[np-1]=="x":
                ListaTerminos.remove(Duplas)
                Terna=[Duplas,i] 
                Mul_Div=1
            else:
                Terna=[float(Numero),i] 
                Numero=str()
                Mul_Div=1
        elif Numero!=str():
            if Mul_Div==0:
                #ERROR?
                Duplas=(float(Numero),"")
                ListaTerminos.append(Duplas)
                Numero=str()
            else:
                Terna.append(float(Numero))
                ListaTerminos.append(Terna) 
                Numero=str()
                Mul_Div=0
        if i == "-":
            Numero = i + Numero
    if Numero!= str():
        if Mul_Div==0:
            Duplas=(float(Numero),"")
            ListaTerminos.append(Duplas)
        else:        
            Terna.append(float(Numero))
            ListaTerminos.append(Terna)
    return ListaTerminos

def Cargar_Lista2(E):
   """"Está función toma una ecuación y la transforma en un lista que contiene tuplas que representan terminos con x y  sin x de la forma (coeficiente, "x") o (coeficiente,"") 
    respectivamente y listas que representan multiplicaciones o divisiones estas listas son de la forma [coeficiente, "*", coeficiente] o [coeficiente,"/", coeficiente] 
    el primer  coeficiente puede ser una tupla si representa un término con x o un float si representa un término sin x. 
    Esta función utiliza cargar lista1 para procesar los elementos dentro de los paréntesis. Los ´parentesis´ son listas que pueden contener tuplas y listas que representan terminos con x y sin x o multiplicaciones o divisiones.
    Además el primer elemento de estas listas es el numero (un float) que multiplica el parentesis el penúltimo elemento es el operador (un string  que es * o /) 
    y el último elemento es un número (un float) por el cual se multiplica o divide el parentesis, estos dos ultimos elementos pueden no estar presentes si el parentesis 
    no está multiplicado (a la derecha del parentesis) o dividido por ningún número.


    Parametros
    ----------
    E : string
        Es la ecuación que se quiere transformar en una lista.

    Returns
    -------
    ListaTerminos : list
    .
    """
   PARENTESIS=[]
   Numero=str()
   Paren=0
   Subcaracter=str()
   ListaTerminos=[]
   Mul_Div=0
   for i, caracter in enumerate(E):
       if Paren==0 and caracter!="(":
#PROCESAMIENTO DE LO QUE ESTÁ FUERA DEL PARENTESIS PARTE 1
          if caracter.isdigit() == True or caracter == '.':
              Numero = Numero+caracter

          elif caracter == "x":
              if Numero==str(): 
                  Duplas=(1,"x")
                  ListaTerminos.append(Duplas)
              elif Numero=="-":
                   Duplas=(-1,"x")
                   ListaTerminos.append(Duplas)
                   Numero=str()
              else:
                   Duplas=(float(Numero),"x") 
                   ListaTerminos.append(Duplas)
                   Numero=str()
              
          elif caracter=="*" or caracter=="/":
              if E[i-1]=="x":
                 ListaTerminos.remove(Duplas)
                 Terna=[Duplas,caracter] 
                 Numero=str()
                 Mul_Div=1
              else:
                    Terna=[float(Numero),caracter] 
                    Numero=str()
                    Mul_Div=1
          elif Numero!=str():
              if Mul_Div==0:
                  Duplas=(float(Numero),"")
                  ListaTerminos.append(Duplas)
                  Numero=str()
              else:
                  Terna.append(float(Numero))
                  ListaTerminos.append(Terna) 
                  Numero=str()
                  Mul_Div=0
          if caracter == "-":
              Numero = caracter +Numero
#PROCESAMIENTO DEL PARENTESIS
        
       if caracter == "(" or Paren==1:
         if  caracter !=")":
             if caracter!="(":
                Subcaracter=Subcaracter+caracter
             if Paren==0: 
                Paren=1
         else:
            PARENTESIS=Cargar_Lista1(Subcaracter)
            if Numero==str():  
               PARENTESIS.insert(0,1)
               Subcaracter=str()
               Numero=str()
               Paren=2
            elif Numero=="-": 
                 PARENTESIS.insert(0,-1)
                 Subcaracter=str()
                 Numero=str()
                 Paren=2
            else:           
                 PARENTESIS.insert(0,float(Numero))
                 Subcaracter=str()
                 Numero=str()
                 Paren=2
                
       if Paren==2:
            if caracter == "/" or caracter == "*":
                PARENTESIS.append(caracter)
                
            elif caracter.isdigit() == True:
                 Numero=Numero+caracter
        
            elif Numero!=str():
                 PARENTESIS.append(float(Numero)) 
                 ListaTerminos.append(PARENTESIS)
                 Numero=str()
                 if caracter=="-":
                    Numero=caracter+Numero 
                 Paren=0
            elif caracter!=")":
                if E[i-1]!="/" and E[i-1]!="*":
                  ListaTerminos.append(PARENTESIS)
                  Subcaracter=str()
                  Numero=str()
                  Paren=0  
                if caracter=="-":
                    Numero=caracter+Numero 
                    
#PROCESAMIENTO DE LO QUE ESTÁ FUERA DEL PARENTESIS PARTE 2
   if Numero!= str() and Paren==0:
      if Mul_Div==0:
         Duplas=(float(Numero),"")
         ListaTerminos.append(Duplas)
      else:        
            Terna.append(float(Numero))
            ListaTerminos.append(Terna)
#PROCESAMIENTO PARENTESIS FINAL
   if Paren==2:
       if Numero!=str():
           PARENTESIS.append(float(Numero))
           ListaTerminos.append(PARENTESIS)
       else:
           ListaTerminos.append(PARENTESIS)
   return ListaTerminos

def Miembros(E):
 """Toma un string y devuelve lista de dos elementos cada elemento es un string que representa  el primer y segundo miembro de la ecuacion"""      
 Miembro=E.split("=")
 return Miembro[0], Miembro[1]  

def Mostrar_Miembro(Lista):
    """ Toma las lista que se crearon en el paso anterior y reconstruye la ecuacón está función se llama a si misma para  mostrar los elementos que están dentro de los paréntesis. 
    Devuelve un string.
    """
    Ecuacion=str()
    for i,Elemento in enumerate(Lista):

      if isinstance(Elemento,tuple)==True:
          if Elemento[0]>=0 and Ecuacion!=str():
             Ecuacion=Ecuacion+"+"+str(Elemento[0])+Elemento[1]
          else:
              Ecuacion=Ecuacion+str(Elemento[0])+Elemento[1]
      if isinstance(Elemento,list)==True:
         if Elemento[1]=="*" or Elemento[1]=="/":
           if isinstance(Elemento[0],tuple)==True: 
            if Elemento[0][0]>=0 and Ecuacion!=str():
               Ecuacion=Ecuacion+"+"+str(Elemento[0][0])+Elemento[0][1]+Elemento[1]+str(Elemento[2])
            else:
                 Ecuacion=Ecuacion+str(Elemento[0][0])+Elemento[0][1]+Elemento[1]+str(Elemento[2])
           
           if isinstance(Elemento[0],float)==True:
              if Elemento[0]>=0 and Ecuacion!=str():
                  Ecuacion=Ecuacion+"+"+str(Elemento[0])+Elemento[1]+str(Elemento[2])
              else:
                    Ecuacion=Ecuacion+str(Elemento[0])+Elemento[1]+str(Elemento[2])
         else:
             Parentesis=[]
             for i in range(len(Elemento)): 
              if isinstance(Elemento[i],(tuple,list)):
                  Parentesis.append(Elemento[i])
             Parentesis=Mostrar_Miembro(Parentesis)
            
             if Elemento[len(Elemento)-2]=="*" or Elemento[len(Elemento)-2]=="/":
                if Elemento[0]>=0 and Ecuacion!=str():
                   Ecuacion=Ecuacion+"+"+str(Elemento[0])+"("+Parentesis+")"+Elemento[len(Elemento)-2]+str(Elemento[len(Elemento)-1])
                else:
                     Ecuacion=Ecuacion+str(Elemento[0])+"("+Parentesis+")"+Elemento[len(Elemento)-2]+str(Elemento[len(Elemento)-1])
             else:
                  if Elemento[0]>=0 and Ecuacion!=str():
                     Ecuacion=Ecuacion+"+"+str(Elemento[0])+"("+Parentesis+")"
                  else:
                       Ecuacion=Ecuacion+str(Elemento[0])+"("+Parentesis+")"
    return Ecuacion

def validarOpcion(opcion,cantidad,limite=1):
    """     "Toma una string y verifica que sea un digito y que esté dentro del rango especificado. Devuelve un booleano"""
    if opcion.isdigit() and int(opcion) >= limite and int(opcion) <= cantidad:
        return True
    else:
        return False
    
def Estandarizar_Numero(numero):
    global Cantidad_Decimales
    numero=numero.replace(",",".")
    return round(float(numero),Cantidad_Decimales)
def normalizar_ecuacion(expr):
    "Elina espacios, convierte a minusculas, elimina operadores repetidos y reemplaza comas por puntos"
    expr = expr.lower()  # X -> x
    expr=expr.replace(",",".")
    # Colapsar operadores repetidos
    # La Barra \ indica que + y * no son cuantificadores de expresiones regulares sino los símbolos 
    # El símbolo + es un cuantificador que indica que el carácter que lo  precede debe aparecer una o más veces (al menos una vez).
    expr = re.sub(r'/+', '/', expr)
    expr = re.sub(r'\*+', '*', expr)
    expr = re.sub(r'\++', '+', expr)
    expr = re.sub(r'-+', '-', expr)
    expr = re.sub(r'x+', 'x', expr)
    expr = re.sub(r'=+', '=', expr)
    return expr
    
    return expr 
def validar_Resultado(ResultadoCargado,ResultadoReal):
    "Toma dos strings y verifica si son equivalentes, es decir si representan el mismo número o el mismo término con x. Devuelve un booleano"
    ResultadoCargado=ResultadoCargado.replace(",",".")
    ResultadoCargado=ResultadoCargado.replace("X","x")
    if ("x" in ResultadoReal) and ("."  in ResultadoCargado):
        Coeficiente=ResultadoCargado.split("x")[0]
        Parteentera=Coeficiente.split(".")[0]
        Partedecimal=Coeficiente.split(".")[1]
        if Parteentera.isdigit() and Partedecimal.isdigit():
           Coeficiente=Estandarizar_Numero(Coeficiente)
           ResultadoReal=Estandarizar_Numero(ResultadoReal.split("x")[0])
           if Coeficiente == ResultadoReal and ("x" in ResultadoCargado):
              return True
           else:
               return False
        else:
             return False
    elif ("." in ResultadoCargado) and ResultadoCargado.split(".")[0].isdigit() and ResultadoCargado.split(".")[1].isdigit():
        ResultadoCargado=Estandarizar_Numero(ResultadoCargado)
        ResultadoReal=Estandarizar_Numero(ResultadoReal)
        if ResultadoCargado == ResultadoReal:
            return True
        else:
            return False 
    elif "x" in ResultadoReal and ResultadoCargado.split("x")[0].isdigit():
        
            Coeficiente=Estandarizar_Numero(ResultadoCargado.split("x")[0])
            ResultadoReal=Estandarizar_Numero(ResultadoReal.split("x")[0])
            if Coeficiente == ResultadoReal and ("x" in ResultadoCargado):
               return True
            else:
                return False
    elif ResultadoCargado.isdigit():
         ResultadoCargado=Estandarizar_Numero(ResultadoCargado)
         ResultadoReal=Estandarizar_Numero(ResultadoReal)
         if ResultadoCargado == ResultadoReal:
             return True
         else:
             return False
    elif ("-" in ResultadoCargado) and ("-" in  ResultadoReal):
       
       return validar_Resultado(ResultadoCargado.split("-")[1], ResultadoReal.split("-")[1]) 
    else:
         return False
def Suma_Resta(Lista,Manual=0):
    """Toma 2 tuplas y las suma o resta, si las tuplas  representan términos con x se pueden sumar o restar entre sí, 
    si representan términos sin x se pueden sumar o restar entre sí pero no se pueden sumar o restar un término con x con un término sin x.
     Modifica la lista  que se ingresa eliminado las tuplas que se suman y represando la por el resultado y 
     devuelve   mensaje  de error si se suman valores que tienen x con sin x"""
    Term1=input("Ingrese el n° del termino que quiera sumar/Restar ")
    Term2=input("Ingrese el otro n° termino que quiera sumar/Restar ")
    if  validarOpcion(Term1,len(Lista)) and validarOpcion(Term2,len(Lista)):
        i=int(Term1)-1
        j=int(Term2)-1    
        Condicion1=isinstance(Lista[i],tuple)
        Condicion2=isinstance(Lista[j],tuple)
        Condicion3=Lista[i][1]==Lista[j][1] and j!=i 
        if Condicion1==True and Condicion2==True:
           if Condicion3==True:
              if Manual==0: 
                  Lista[i]=(Lista[i][0]+Lista[j][0],Lista[i][1])
                  Lista.pop(j)
              else:
                   Resultado=input(f"Ingrese el resultado de {Mostrar_Miembro([Lista[i],Lista[j]])} ")
                   if Lista[i][1]=="x" and validar_Resultado(Resultado,str(Lista[i][0]+Lista[j][0])+"x"):
                      Lista[i]=(Lista[i][0]+Lista[j][0],Lista[i][1])
                      Lista.pop(j)  
                   elif Lista[i][1]=="" and validar_Resultado(Resultado,str(Lista[i][0]+Lista[j][0])):
                       Lista[i]=(Lista[i][0]+Lista[j][0],Lista[i][1])
                       Lista.pop(j) 
              return""
           else:
               return"No se puede sumar términos con x con términos sin x, o un mismo termino dos veces"
        else:
           return "No se puede sumar términos si tienen un parentesis o si en los términos hay una multiplición"
    else:
        return"Uno de la de los términos seleccionados no existe"
             
def Gestionar_Historial(Lista1,Lista2,Historial,Paso=-1):
    """ Guarda todas las listas que se van generando a lo largo de la resolución de la ecuación en una lista llamada historial,
      esta lista es una lista de listas cada elemento es una lista que contiene 
    dos elementos que son las listas que representan el primer y segundo miembro de la ecuación. Además permite volver a un paso anterior de la resolución de la ecuación 
    ingresando el número del paso al que se quiere volver, esto se hace eliminando los pasos posteriores al paso al que se quiere volver y reemplazando las listas actuales 
    del primer y segundo miembro por las listas que estaban en el paso al que se quiere volver."""
    i=len(Historial)-1
    Copia1=Lista1
    Copia1=copy.deepcopy(Lista1)
    Copia2=copy.deepcopy(Lista2)
    
    if Historial==[]:
       Historial.append([Copia1,Copia2])  
    elif Historial[i]!=[Copia1,Copia2]:
         Historial.append([Copia1,Copia2])
         
    if Paso!=-1:
       Paso=input("Ingrese al paso que quiere volver ingrese cero para no modificar nada ")
       if validarOpcion(Paso,len(Historial),0):
           Paso=int(Paso)
           if Paso!=0:
               Lista1[:]=Historial[Paso-1][0].copy()
               Lista2[:]=Historial[Paso-1][1].copy()
               while i>(Paso-1):
                  Historial.pop(i)
                  i=i-1
   

def imprimir(Historial):
  """Crea un string con las distintas ecuaciones equivalentes que se fueron generando a lo largo de la resolución de la ecuación.
  Toma como entrada el historial que produce la función gestionar historial"""
  A=str()
  for i, miembro in enumerate(Historial):
     A=A+"\n"+f"Paso {i+1} {Mostrar_Miembro(miembro[0])}={Mostrar_Miembro(miembro[1])}"
  return A

def Condicion_de_corte(Lista1,Lista2):
 if Lista1==[(1,"x")] and len(Lista2)==1 and Lista2[0][1]=="":
    return True, f"La solución de la ecuación es x={Lista2[0][0]}"
 elif Lista1==[(0,"x")] and len(Lista2)==1 and Lista2[0][1]=="" and Lista2[0][0]==0:
    return True, f"La 0x={Lista2[0][0]} x puede ser cualquier valor ya que cualquier número multiplicado por cero da cero"
 elif Lista1==[(0,"x")] and len(Lista2)==1 and Lista2[0][1]=="":
     return True, f"La 0x={Lista2[0][0]} no hay nigún valdor de x que cumpla la igualdad ya que cualquier número multiplicado por cero da cero"
 else:
     return False,""
 
def Multiplicacion(Lista,Manual=0):
 """Esta función toma las listas que representan un miembro y resuelve las multiplicaciones reemplazando las lista de multiplicaciones por una tupla 
    que representa el resultado en la lista de miembros en la misma posición.
    Manual=0 significa que las multiplicaciones se pueden resolver automaticamente y permite saltar una multiplicación si el resultado es incorrecto,
    Manual=1 significa que se resuelven manualmente y no se puede saltar ninguna multiplicación"""
 j=1
 while j!=0:
  j=0
  I=[]
  Salto="0"
  OPCION=""
  a="Valor,Incial"
  OP=""
  for i, M in enumerate(Lista):
      if isinstance(M,list) and M[1]=="*":
         j=j+1
         I.append(i)
         if isinstance(M[0],tuple):
            OPCION=OPCION+"\n"+ f"{j}) {M[0][0]}{M[0][1]}{M[1]}{M[2]} "
         else:
              OPCION=OPCION+"\n"+ f"{j}) {M[0]}{M[1]}{M[2]} "
  if Manual==1 and j!=0:
     OP=input("Ingrese el numero de la cuenta que quiera resolver"+"\n"+OPCION+"\n" )
     
  elif j!=0:
      OP=input("Ingrese el numero de la cuenta que quiera"+"\n"+OPCION+"\n"+str(j+1)+")"+"Resolver todas la muliplicaciones\n ")

  if  validarOpcion(OP,j): 
     OP=int(OP)
     if isinstance(Lista[I[OP-1]][0],tuple)==True:
         while validar_Resultado(a, str(Lista[I[OP-1]][0][0]*Lista[I[OP-1]][2])+"x")!=True and Salto=="0":
         
             a=input(f"ingrese el resultado de la {Lista[I[OP-1]][0][0]}{Lista[I[OP-1]][0][1]}*{Lista[I[OP-1]][2]} ")
          
             if validar_Resultado(a, str(Lista[I[OP-1]][0][0]*Lista[I[OP-1]][2])+"x")!=True and Manual==0:
              Salto=input("Resultado incorreto para volver hacerla marca cero (0) para saltar la cuenta 1 ")
    
         Lista[I[OP-1]]=(Lista[I[OP-1]][0][0]*Lista[I[OP-1]][2],"x")
      
    
       
     else:
         while validar_Resultado(a, str(Lista[I[OP-1]][0]*Lista[I[OP-1]][2]))!=True and Salto=="0":
              
           a=input(f"ingrese el resultado de la {Lista[I[OP-1]][0]}*{Lista[I[OP-1]][2]} ")
           
           if validar_Resultado(a, str(Lista[I[OP-1]][0]*Lista[I[OP-1]][2]))!=True and Manual==0: 
              Salto=input("Hubo un error  en las cuentas para volver hacerla marque 0 (cero) para saltar la cuenta 1 ")
          
         Lista[I[OP-1]]=(Lista[I[OP-1]][0]*Lista[I[OP-1]][2],"")
          
  elif validarOpcion(OP,j+1) and Manual==0:
      for i in I:
          if isinstance(Lista[i][0],tuple)==True:
             Lista[i]=(Lista[i][0][0]*Lista[i][2],Lista[i][0][1])
          else:
             Lista[i]=(Lista[i][0]*Lista[i][2],"")

def Division(Lista,Manual=0):
 """Esta función toma las listas que representan un miembro y resuelve las divisiones reemplazando las lista 
    de divisiones por una tupla que representa el resultado en la lista de miembros en la misma posición. Tiene al igual que la función multiplicación dos modos Manual=0 y Manual=1. 
    Devuelve un mensaje de que la ecuación no tiene solución si se intenta dividir por cero"""
 j=1

 while j!=0:
  j=0
  I=[]
  Salto="0"
  OPCION=""
  a=""
  OP=""
  for i, M in enumerate(Lista):
      if isinstance(M,list) and M[1]=="/":
         j=j+1
         I.append(i)
         if isinstance(M[0],tuple):
            OPCION=OPCION+"\n"+ f"{j}) {M[0][0]}{M[0][1]}{M[1]}{M[2]} "
         else:
              OPCION=OPCION+"\n"+ f"{j}) {M[0]}{M[1]}{M[2]} "
  if Manual==1 and j!=0:
     OP=input("Ingrese el numero de la cuenta que quiera resolver"+"\n"+OPCION )
  elif j!=0:
      OP=input("Ingrese el numero de la cuenta que quiera"+"\n"+OPCION+"\n"+str(j+1)+")"+"Resolver todas las divisiones ")
    
  if validarOpcion(OP,j) and Lista[I[int(OP)-1]][2]!=0: 
     OP=int(OP)
     if isinstance(Lista[I[OP-1]][0],tuple)==True:
        while validar_Resultado(a, str(Lista[I[OP-1]][0][0]/Lista[I[OP-1]][2])+"x")!=True and Salto=="0":
       
          a=input(f"ingrese el resultado de la {Lista[I[OP-1]][0][0]}{Lista[I[OP-1]][0][1]}/{Lista[I[OP-1]][2]} ")
          
          if validar_Resultado(a, str(Lista[I[OP-1]][0][0]/Lista[I[OP-1]][2])+"x")!=True and Manual==0:
             Salto=input("Hubo un error  en las cuentas para volver hacerla marque cero (0) para saltar la cuenta 1 ")
        Lista[I[OP-1]]=(Lista[I[OP-1]][0][0]/Lista[I[OP-1]][2],"x")
       
     else:
          while validar_Resultado(a, str(Lista[I[OP-1]][0]/Lista[I[OP-1]][2]))!=True and Salto=="0":
          #while a!=f"{Lista[I[OP-1]][0]/Lista[I[OP-1]][2]}" and Salto==0:    
           a=input(f"ingrese el resultado de la {Lista[I[OP-1]][0]}/{Lista[I[OP-1]][2]} ")
          
           if validar_Resultado(a, str(Lista[I[OP-1]][0]/Lista[I[OP-1]][2]))!=True and Manual==0:
               
              Salto=input("Hubo un error  en las cuentas para volver hacerla marque 0 (cero) para saltar la cuenta 1 ")
          
          Lista[I[OP-1]]=(Lista[I[OP-1]][0]/Lista[I[OP-1]][2],"")
  elif validarOpcion(OP,j) and Lista[I[int(OP)-1]][2]==0:
       print("No se puede dividir por cero.Que haya una división por cero significa que la ecuación no tiene solución.")    
       j=0
  elif validarOpcion(OP,j+1) and Manual!=1:
      for i in I:
          if isinstance(Lista[i][0],tuple)==True and Lista[i][2]!=0:
             Lista[i]=(Lista[i][0][0]/Lista[i][2],Lista[i][0][1])
          elif Lista[i][2]!=0:
             Lista[i]=(Lista[i][0]/Lista[i][2],"")
          else:
                print("No se puede dividir por cero.Que haya una división por cero significa que la ecuación no tiene solución.")
                j=0

def Distributividad(Lista):
    """Esta función toma las listas que representan un miembro y resuelve la distributividad reemplazando las lista de paréntesis por tuplas que representan el resultado en la lista de miembros en la misma posición.
     Para esto se multiplica o divide cada término dentro del paréntesis por el número que multiplica o divide al paréntesis dependiendo de si el paréntesis está multiplicado o dividido por un número. 
     Devuelve un mensaje de que la ecuación no tiene solución si se intenta dividir por cero."""
    OPCION1=""
    j=0
    I=[]
    
    for i,Parentesis in enumerate(Lista):
        if isinstance(Parentesis,list) and Parentesis[1]!="/" and Parentesis[1]!="*": 
           j=j+1
           OPCION1=OPCION1+"\n"+str(j)+")"+Mostrar_Miembro([Parentesis])
           I.append(i)
    if j!=0:       
        N=input("Elija el parentesis que quiera resolver \n" +OPCION1+"\n")
    if  validarOpcion(N, j): 
        N=int(N)
        Parentesis=Lista[I[N-1]]
        L=len(Parentesis)

        for k, Termino in enumerate(Parentesis):
        
            if  Parentesis[L-1]!=0 and "/" in Parentesis:
                if isinstance(Termino ,tuple):
                   Parentesis[k] =((Parentesis[0]/Parentesis[L-1])*Termino[0], Termino[1])
                elif  isinstance(Termino ,list):
                      if isinstance(Termino[0],float):   
                          Parentesis[k][0]=(Parentesis[0]/Parentesis[L-1])*Termino[0]
                      else:
                           Parentesis[k][0]=((Parentesis[0]/Parentesis[L-1])*Termino[0][0],"x")
                            
            elif Parentesis[L-1]==0 and "/" in Parentesis:
                 print("No se puede resolever una división por cero, por lo tanto la ecuación no tiene solución")
            elif "*" in Parentesis:
                if isinstance(Termino ,tuple): 
                   Parentesis[k] =((Parentesis[0]*Parentesis[L-1])*Termino[0], Termino[1])
                elif  isinstance(Termino ,list):
                    if isinstance(Termino[0],float):   
                        Parentesis[k][0]=(Parentesis[0]*Parentesis[L-1])*Termino[0]
                    else:
                         Parentesis[k][0]=((Parentesis[0]*Parentesis[L-1])*Termino[0][0],"x")
           
            else:
                if isinstance(Termino ,tuple):
                    Parentesis[k] =(Parentesis[0]*Termino[0], Termino[1])
                elif  isinstance(Termino ,list):
                        if isinstance(Termino[0],float):   
                            Parentesis[k][0]=Parentesis[0]*Termino[0]
                        else:
                             Parentesis[k][0]=(Parentesis[0]*Termino[0][0],"x")
        j=0          
        for Termino in Parentesis.copy():
     
            if isinstance(Termino,tuple) or isinstance(Termino,list):
                Lista.insert(I[N-1]+j,Termino)
                j=j+1
        Lista.pop(I[N-1]+j)
        
def Distributividad_Manual(Lista):
    "Modifica la lista de miembros aplicando la propiedad distributiva"""
    OPCION1=""
    j=0
    I=[]
   
    
    for i,Parentesis in enumerate(Lista):
        if isinstance(Parentesis,list) and Parentesis[1]!="/" and Parentesis[1]!="*": 
           j=j+1
           OPCION1=OPCION1+"\n"+str(j)+")"+Mostrar_Miembro([Parentesis])
           I.append(i)
    if j!=0:       
        N=input("Elija el parentesis que quiera resolver \n" +OPCION1+"\n")
        if validarOpcion(N, j):  
            N=int(N)
            Parentesis=Lista[I[N-1]]
            Copia=Parentesis.copy()
            L=len(Parentesis)
            k=0
            A=""
            for i, Termino in enumerate(Copia):
        
                if  Copia[L-1]!=0 and "/" in Copia:
                    if  isinstance(Termino ,tuple) and Copia[0]==1:
                    
                        if "x" in Termino:
                            Lista.insert(I[N-1]+k,[Termino,"/",Copia[L-1]])
                        else:
                            Lista.insert(I[N-1]+k,[Termino[0],"/",Copia[L-1]])
                        k=k+1
                    elif isinstance(Termino ,tuple):
                        while validar_Resultado(A,str(Copia[0]/Copia[L-1]))==False:
                              A=input(f"Calcule la división {Copia[0]}/{Copia[L-1]} ")
                        if "x" in Termino:
                            Lista.insert(I[N-1]+k,[Termino,"*",Copia[0]/Copia[L-1]])
                        else:
                              Lista.insert(I[N-1]+k,[Termino[0],"*",Copia[0]/Copia[L-1]])
                        k=k+1
                    elif isinstance(Termino ,list):
                    
                      if isinstance(Termino[0],float):   
                          while validar_Resultado(A,str(Copia[0]/Copia[L-1]*Termino[0]))==False:
                                A=input(f"Calcule  ({Copia[0]}/{Copia[L-1]})*{Termino[0]} ")
                          Copia[i][0]=(Copia[0]/Copia[L-1])*Termino[0]
                          Lista.insert(I[N-1]+k,Termino)
                          k=k+1
                      else:
                          while validar_Resultado(A,str((Copia[0]/Copia[L-1])*Termino[0][0])+"x")==False:
                                 A=input(f"Calcule ({Copia[0]}/{Copia[L-1]})*{Termino[0][0]}x ")
                          Copia[i][0]=((Copia[0]/Copia[L-1])*Termino[0][0],"x")
                          Lista.insert(I[N-1]+k,Termino)
                          k=k+1   
                elif Copia[L-1]==0 and "/" in Copia:
                     print("No se puede resolever una división por cero, por lo tanto la ecuación no tiene solución")
                elif "*" in Copia:
    
                    if isinstance(Termino ,tuple):
                        while validar_Resultado(A,str(Copia[0]*Copia[L-1]))==False:
                              A=input(f"Calcule la multiplicación {Copia[0]}*{Copia[L-1]} ")
                        if "x" in Termino:
                           
                            Lista.insert(I[N-1]+k,[Termino,"*",Copia[0]*Copia[L-1]])
                        else:
                                Lista.insert(I[N-1]+k,[Termino[0],"*",Copia[0]*Copia[L-1]])
                        k=k+1
                            
                    elif  isinstance(Termino ,list):
                    
                      if isinstance(Termino[0],float):   
                         while validar_Resultado(A,str(Copia[0]*Copia[L-1]*Termino[0]))==False: 
                               A=input(f"Calcule  {Copia[0]}*{Copia[L-1]}*{Termino[0]} ")
                             
                         Copia[i][0]=(Copia[0]*Copia[L-1])*Termino[0]
                         Lista.insert(I[N-1]+k,Termino)
                         k=k+1
                      else:
                          while validar_Resultado(A,str(Copia[0]*Copia[L-1]*Termino[0][0])+"x")==False:
                                A=input(f"Calcule {Copia[0]}*{Copia[L-1]}*{Termino[0][0]}x ")
                          Copia[i][0]=((Copia[0]*Copia[L-1])*Termino[0][0],"x")
                          Lista.insert(I[N-1]+k,Termino)
                          k=k+1
                else:
                    if isinstance(Termino,tuple):
                 
                        if "x" in Termino:
                            
                            Lista.insert(I[N-1]+k,[Termino,"*",Copia[0]])
                        else:
                            Lista.insert(I[N-1]+k,[Copia[0],"*", Termino[0]]) 
                        k=k+1
                    elif  isinstance(Termino,list):
                    
                          if isinstance(Termino[0],float):  
                             while validar_Resultado(A, str(Copia[0]*Termino[0]))==False:
                                  A=input(f"Ingresa el resultado de la multiplicación {Copia[0]}*{Termino[0]} ")   
                             
                             Copia[i][0]=Copia[0]*Termino[0]
                             Lista.insert(I[N-1]+k,Termino)
                             k=k+1
                          else:
                              while  validar_Resultado(A, str(Copia[0]*Termino[0][0])+"x")==False:
                                     A=input(f"Ingresa el resultado de la multiplicación {Copia[0]}*{Termino[0][0]}x ")
                              print(validar_Resultado(A, str(Copia[0]*Termino[0][0])+"x"))
                              Copia[i][0]=(Copia[0]*Termino[0][0],"x")
                              Lista.insert(I[N-1]+k,Termino)
                              k=k+1           
            Lista.pop(I[N-1]+k)  

def Opuesto(Lista1,Lista2):
 
 a=""
 for i, Termino in enumerate(Lista1):
  if isinstance(Termino[0],tuple):
      if Termino[0][0]>=0:
        a=a+"\n"f"Pasar {Mostrar_Miembro([Termino])} restando"
      else:
            a=a+"\n"f"{i+1} Pasar {Mostrar_Miembro([Termino])} sumando "
  else:
        if Termino[0]>=0:
              a=a+"\n"f"{i+1} Pasar {Mostrar_Miembro([Termino])} restando "
        else:
              a=a+"\n"f"{i+1} Pasar {Mostrar_Miembro([Termino])} sumando "   
 OP=input(a+" \n")
 if validarOpcion(OP,i+1): 
    N=int(OP)-1
    if isinstance(Lista1[N],tuple):
        Lista2.append((-Lista1[N][0],Lista1[N][1]))
        Lista1.pop(N)
    elif isinstance(Lista1[N],list) and isinstance(Lista1[N][0],tuple):
        Lista1[N][0]=(-Lista1[N][0][0],Lista1[N][0][1])
        Lista2.append(Lista1[N])
        Lista1.pop(N)
    else:
        Lista1[N][0]=-Lista1[N][0]
        Lista2.append(Lista1[N])
        Lista1.pop(N)
    if Lista1==[]:
       Lista1.append((0,""))

def Inverso(Lista1,Lista2):
  Copia=Lista1.copy()
  if isinstance(Lista1[0],tuple) and "x" in Lista1[0]:
     if "x" in Lista2[0]:
       Lista2[0]=[Lista2[0],"/",Lista1[0][0]]
       Lista1[0]=(1,"x")
     else:
         Lista2[0]=[Lista2[0][0],"/",Lista1[0][0]]
         Lista1[0]=(1,"x")
         
  elif not("/"  in Lista1[0])  and not ( "*"  in Lista1[0]): 
       Lista1.remove(Lista1[0])  
       for Termino in Copia[0]:
         if isinstance(Termino,(tuple,list)): 
           Lista1.append(Termino)
       if "x" in Lista2[0]:
              Lista2[0]=[Lista2[0],"/",Copia[0][0]]
       else:
               Lista2[0]=[Lista2[0][0],"/",Copia[0][0]]
         
  elif Lista1[0][len(Lista1[0])-2]=="/" and ((len(Lista1[0])!=3 and Lista1[0][0]==1) or isinstance(Lista1[0][0],tuple)):
       Lista1.remove(Lista1[0])
       for Termino in Copia[0]:
           if isinstance(Termino,(tuple,list)): 
               Lista1.append(Termino)
       if "x" in Lista2[0]:
          Lista2[0]=[Lista2[0],"*",Copia[0][len(Copia[0])-1]]
       else:
           Lista2[0]=[Lista2[0][0],"*",Copia[0][len(Copia[0])-1]]
           

def Lista_Opciones(Lista1,Lista2):
    I=[]
    PARENTESIS=0
    Mult=0
    Div=0
    Suma=0
    i=0
    Texto="Elija la opción que quiera"
    for termino in Lista1:
        if isinstance(termino,tuple):
            Suma=Suma+1
            if Suma==2:
               i=i+1
               Texto=Texto+"\n"+f"{i}) Sumar/Restar Términos"
               I.append([i,"Suma"])
        elif isinstance(termino,list) and termino[1]=="*" and Mult!=1:
             Mult=Mult+1
             i=i+1
             Texto=Texto+"\n"+f"{i}) Resolver multiplicaciones"
             I.append([i,"Multiplicación"])
        elif isinstance(termino,list) and termino[1]=="/"and Div!=1:
             Div=Div+1
             i=i+1
             Texto=Texto+"\n"+f"{i}) Resolver divisiones"
             I.append([i,"División"])
        elif isinstance(termino,list) and termino[1]!="/" and termino[1]!="*" and  PARENTESIS!=1:
             PARENTESIS=PARENTESIS+1
             i=i+1
             Texto=Texto+"\n"+f"{i}) Eliminar parentesis"
             I.append([i,"Distributiva"])
    if  len(Lista1)==1 and len(Lista2)==1 and isinstance(Lista2[0],tuple):

        if isinstance(Lista1[0],(tuple)):  
            i=i+1
            Texto=Texto+"\n"+f"{i}) pasar dividiendo{Lista1[0][0]}"
            I.append([i,"Inverso"])
            
        elif ((Lista1[0][0]==1 and len(Lista1[0])!=3) or isinstance(Lista1[0][0],tuple))  and Lista1[0][len(Lista1[0])-2]=="/":      
            i=i+1
            Texto=Texto+"\n"+f"{i}) pasar Multiplicando{Lista1[0][len(Lista1[0])-1]}" 
           
            I.append([i,"Inverso"])
        elif not("/"  in Lista1[0])  and not("*"  in Lista1[0]):  
            i=i+1
            Texto=Texto+"\n"+f"{i}) pasar dividiendo{Lista1[0][0]}"
            I.append([i,"Inverso"])    
    i=i+1
    Texto=Texto+"\n"+f"{i}) Pasar terminos al otro lado con la operación contraria"
    I.append([i,"Opuesto"])
    i=i+1
    Texto=Texto+"\n"+f"{i}) Volver a elegir Miembro"
    I.append([i,"Miembro"])
    i=i+1
    Texto=Texto+"\n"+f"{i}) Volver a un paso anterior"
    I.append([i,"Historial"])
    return Texto,I
def Lista_Opciones2(A,B,OP2,I,Manual):
    """ A representa la lista(miembro) que se va trabajar"""
    if validarOpcion(OP2, len(I)):
        OP2=int(OP2)
        if I[OP2-1][1]=="Suma":
            print(Suma_Resta(A,Manual))
        elif I[OP2-1][1]=="Multiplicación":
             Multiplicacion(A,Manual)
            
        elif I[OP2-1][1]=="División":
             Division(A,Manual)
        
        elif I[OP2-1][1]=="Distributiva":
            if Manual==0:
                  Distributividad(A)
            else:
                  Distributividad_Manual(A)
        elif I[OP2-1][1]=="Inverso":
             Inverso(A,B)
        elif I[OP2-1][1]=="Opuesto":
             Opuesto(A,B)
def OPCIONES(Manual):    
    Ecuación=input("Ingrese la ecuación que quiera resolver \n")
    Ecuación=normalizar_ecuacion(Ecuación)
    if "="in Ecuación and Miembros(Ecuación)[1]!="":
        M1,M2=Miembros(Ecuación)
        Lista1=Cargar_Lista2(M1)
        Lista2=Cargar_Lista2(M2)
        Historial=[]
        OP1=""
        
        while Condicion_de_corte(Lista1, Lista2)[0]==False and Condicion_de_corte(Lista2, Lista1)[0]==False and OP1!="3":
             Gestionar_Historial(Lista1, Lista2, Historial,-1)
             print(imprimir(Historial))
             OP1=input(
                 f"""Seleccione que el miembro quiere trabajar:
                          
                     1) Primer miembro {Mostrar_Miembro(Lista1)}
         
                     2) Segundo Miembro {Mostrar_Miembro(Lista2)} 
                           
                     3) Cargar otra ecuación\n """)
             if OP1=="1":
                        Texto,I=Lista_Opciones(Lista1,Lista2) 
                        
                        OP2=input(Texto+"\n" )  
                        Lista_Opciones2(Lista1, Lista2, OP2, I,Manual)
             elif OP1=="2":
                       Texto,I=Lista_Opciones(Lista2, Lista1)
                       OP2=input(Texto+"\n" )
                       Lista_Opciones2(Lista2, Lista1, OP2, I,Manual)
    
             if OP1!="3"and validarOpcion(OP2,len(I)) and I[int(OP2)-1][1]=="Historial":
                Gestionar_Historial(Lista1, Lista2, Historial,1)
                
        if Condicion_de_corte(Lista1, Lista2)[0]:
            print(Condicion_de_corte(Lista1, Lista2)[1])
        if Condicion_de_corte(Lista2, Lista1)[0]:
            print(Condicion_de_corte(Lista2, Lista1)[1])
            
        input("Presione enter para salir")
    else:
        "Te olvidaste de poner el = y/o escribir el segundo miembro"
def Menu():
    A="1" 
    #1=Modo Manual activado
    Manual=0 
    while A!="5":
        A=input(     
"""                              MENÚ 

                        1) Resolver ecuaciones
            
                        2) Modo Automático:
    
       En este modo las sumas y resta se resuelven solas, las divisiones y 
       multiplicaciones se pueden resolver haciendo las cuentas  
       o automáticamente, también se pueden saltar la cuentas, en caso de que 
       te trabes. Es el modo por defecto.
       
                           3) Modo Manual: 
               
                Las cuentas hay que resolverla manualmente.
                    
              
                        4) Cantidad de decimales:
    
       Para comprobar que se hicieron bien la cuentas el programa toma una 
       cierta cantidad de decimales, por defecto redondea en 2 decimales,
       Para cambiar la cantidad de decimales apreta usa esta opción. 
       Las cuentas se hacen  con una cantidad fija que no cambia lo que cambia
       es la cantidad de decimales que se usan para comprobar un resultado
                       5) Salir \n """)
        if A=="1":
          OPCIONES(Manual)
        elif A=="2":
            Manual=0
        elif A=="3":
             Manual=1
        elif A=="4" :
            B=input("Ingresa la cantidad decimales para validar la cuenta ")
            if B.isdigit():
                global Cantidad_Decimales
                Cantidad_Decimales=int(B)

Menu()
#EVITAR QUE SE INGRESEN COSAS INCORRECTAS (validar tiene algunas expeciones si se mezclan resultado correctos e incorrectos)

#Corregir
