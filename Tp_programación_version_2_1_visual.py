# -*- coding: utf-8 -*-
"""
ECUACIÓN PARENTESIS
"""
import copy 
import re
import os
Cantidad_Decimales=2

# ============================================================
#  ESTILO VISUAL: colores, símbolos matemáticos y cajas
# ============================================================
# Habilita los códigos ANSI de color en la consola de Windows (cmd/PowerShell)
os.system("")

class Estilo:
    RESET   = "\033[0m"
    NEGRITA = "\033[1m"
    TENUE   = "\033[2m"
    CIAN    = "\033[96m"
    VERDE   = "\033[92m"
    AMARILLO= "\033[93m"
    ROJO    = "\033[91m"
    MAGENTA = "\033[95m"
    AZUL    = "\033[94m"
    GRIS    = "\033[90m"

def formatear_numero(numero):
    """Convierte 3.0 -> '3', -2.5 -> '-2,5' (estilo numérico es-AR, sin .0 de más)."""
    try:
        n = float(numero)
    except (TypeError, ValueError):
        return str(numero)
    if n == int(n):
        texto = str(int(n))
    else:
        texto = f"{n:.10f}".rstrip("0").rstrip(".")
    return texto.replace(".", ",")

def embellecer_ecuacion(texto):
    """Reemplaza operadores de texto plano por símbolos matemáticos prolijos
    y normaliza signos +- pegados, solo para mostrar en pantalla."""
    t = texto
    t = t.replace("*", " × ")
    t = t.replace("/", " ÷ ")
    t = t.replace("+-", " − ")
    t = t.replace("-", " − ")
    t = t.replace("+", " + ")
    # Colapsar espacios múltiples
    t = re.sub(r" +", " ", t).strip()
    # Si el signo negativo queda al principio, pegarlo al número (-2x, no - 2x)
    t = re.sub(r"^− ", "−", t)
    t = re.sub(r"(\(|› )− ", r"\1−", t)
    # Prolijidad alrededor de paréntesis
    t = t.replace("( ", "(").replace(" )", ")")
    return t

def caja_ecuacion(texto, titulo=None, color=Estilo.CIAN):
    """Dibuja la ecuación (u otro texto corto) dentro de una caja con bordes Unicode."""
    lineas = texto.split("\n")
    ancho = max(len(l) for l in lineas + ([titulo] if titulo else [""]))
    ancho = max(ancho, 10) + 2
    salida = []
    if titulo:
        salida.append(f"{color}╭─ {Estilo.NEGRITA}{titulo}{Estilo.RESET}{color} {'─'*(ancho-len(titulo)-3)}╮{Estilo.RESET}")
    else:
        salida.append(f"{color}╭{'─'*ancho}╮{Estilo.RESET}")
    for l in lineas:
        relleno = ancho - len(l) - 1
        salida.append(f"{color}│{Estilo.RESET} {Estilo.NEGRITA}{l}{Estilo.RESET}{' '*relleno}{color}│{Estilo.RESET}")
    salida.append(f"{color}╰{'─'*ancho}╯{Estilo.RESET}")
    return "\n".join(salida)

def titulo_seccion(texto, color=Estilo.AMARILLO):
    return f"\n{color}{Estilo.NEGRITA}── {texto} ──{Estilo.RESET}"

def Cargar_Lista1(E):
    """
    Está función toma una ecuación y la transforma en un lista que contiene 
    d

    Parameters
    ----------
    E : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
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
 """Divide la ecuación en dos miebros devuelve una cadena de 
 caracteres del primer y segundo miebro"""      
 Miembro=E.split("=")
 return Miembro[0], Miembro[1]  

def Mostrar_Miembro(Lista):
    Ecuacion=str()
    for i,Elemento in enumerate(Lista):

      if isinstance(Elemento,tuple)==True:
          if Elemento[0]>=0 and Ecuacion!=str():
             Ecuacion=Ecuacion+"+"+formatear_numero(Elemento[0])+Elemento[1]
          else:
              Ecuacion=Ecuacion+formatear_numero(Elemento[0])+Elemento[1]
      if isinstance(Elemento,list)==True:
         if Elemento[1]=="*" or Elemento[1]=="/":
           if isinstance(Elemento[0],tuple)==True: 
            if Elemento[0][0]>=0 and Ecuacion!=str():
               Ecuacion=Ecuacion+"+"+formatear_numero(Elemento[0][0])+Elemento[0][1]+Elemento[1]+formatear_numero(Elemento[2])
            else:
                 Ecuacion=Ecuacion+formatear_numero(Elemento[0][0])+Elemento[0][1]+Elemento[1]+formatear_numero(Elemento[2])
           
           if isinstance(Elemento[0],float)==True:
              if Elemento[0]>=0 and Ecuacion!=str():
                  Ecuacion=Ecuacion+"+"+formatear_numero(Elemento[0])+Elemento[1]+formatear_numero(Elemento[2])
              else:
                    Ecuacion=Ecuacion+formatear_numero(Elemento[0])+Elemento[1]+formatear_numero(Elemento[2])
         else:
             Parentesis=[]
             for i in range(len(Elemento)): 
              if isinstance(Elemento[i],(tuple,list)):
                  Parentesis.append(Elemento[i])
             Parentesis=Mostrar_Miembro(Parentesis)
            
             if Elemento[len(Elemento)-2]=="*" or Elemento[len(Elemento)-2]=="/":
                if Elemento[0]>=0 and Ecuacion!=str():
                   Ecuacion=Ecuacion+"+"+formatear_numero(Elemento[0])+"("+Parentesis+")"+Elemento[len(Elemento)-2]+formatear_numero(Elemento[len(Elemento)-1])
                else:
                     Ecuacion=Ecuacion+formatear_numero(Elemento[0])+"("+Parentesis+")"+Elemento[len(Elemento)-2]+formatear_numero(Elemento[len(Elemento)-1])
             else:
                  if Elemento[0]>=0 and Ecuacion!=str():
                     Ecuacion=Ecuacion+"+"+formatear_numero(Elemento[0])+"("+Parentesis+")"
                  else:
                       Ecuacion=Ecuacion+formatear_numero(Elemento[0])+"("+Parentesis+")"
    return Ecuacion

def Mostrar_Bonito(Lista):
    """Versión embellecida de Mostrar_Miembro: misma ecuación, pero con
    símbolos matemáticos lindos (×, ÷, −) y espaciado prolijo, lista para
    mostrar en pantalla. Es solo una capa visual, no se usa para validar nada."""
    return embellecer_ecuacion(Mostrar_Miembro(Lista))

def validarOpcion(opcion,cantidad,limite=1):
    if opcion.isdigit() and int(opcion) >= limite and int(opcion) <= cantidad:
        return True
    else:
        return False
    
def Estandarizar_Numero(numero):
    global Cantidad_Decimales
    numero=numero.replace(",",".")
    return round(float(numero),Cantidad_Decimales)
def normalizar_ecuacion(expr):
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
                   Resultado=input(f"{Estilo.AMARILLO}Ingrese el resultado de {Estilo.RESET} {Estilo.NEGRITA}{Mostrar_Bonito([Lista[i],Lista[j]])}{Estilo.RESET} ")
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
  A=str()
  for i, miembro in enumerate(Historial):
     ecuacion=f"{Mostrar_Bonito(miembro[0])}  =  {Mostrar_Bonito(miembro[1])}"
     es_ultimo = (i == len(Historial)-1)
     color = Estilo.VERDE if es_ultimo else Estilo.GRIS
     A=A+"\n"+caja_ecuacion(ecuacion, titulo=f"Paso {i+1}", color=color)
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
      #while a!=f"{Lista[I[OP-1]][0][0]/Lista[I[OP-1]][2]}x" and Salto==0:    
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
    OPCION1=""
    j=0
    I=[]
    
    for i,Parentesis in enumerate(Lista):
        if isinstance(Parentesis,list) and Parentesis[1]!="/" and Parentesis[1]!="*": 
           j=j+1
           OPCION1=OPCION1+"\n"+f"{Estilo.CIAN}{j}){Estilo.RESET} "+Mostrar_Bonito([Parentesis])
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
    OPCION1=""
    j=0
    I=[]
   
    
    for i,Parentesis in enumerate(Lista):
        if isinstance(Parentesis,list) and Parentesis[1]!="/" and Parentesis[1]!="*": 
           j=j+1
           OPCION1=OPCION1+"\n"+f"{Estilo.CIAN}{j}){Estilo.RESET} "+Mostrar_Bonito([Parentesis])
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
        a=a+"\n"f"Pasar {Mostrar_Bonito([Termino])} restando"
      else:
            a=a+"\n"f"{Estilo.CIAN}{i+1}){Estilo.RESET} Pasar {Mostrar_Bonito([Termino])} sumando "
  else:
        if Termino[0]>=0:
              a=a+"\n"f"{Estilo.CIAN}{i+1}){Estilo.RESET} Pasar {Mostrar_Bonito([Termino])} restando "
        else:
              a=a+"\n"f"{Estilo.CIAN}{i+1}){Estilo.RESET} Pasar {Mostrar_Bonito([Termino])} sumando "   
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
    Texto=f"{Estilo.AZUL}{Estilo.NEGRITA}Elija la opción que quiera:{Estilo.RESET}"
    for termino in Lista1:
        if isinstance(termino,tuple):
            Suma=Suma+1
            if Suma==2:
               i=i+1
               Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Sumar/Restar términos"
               I.append([i,"Suma"])
        elif isinstance(termino,list) and termino[1]=="*" and Mult!=1:
             Mult=Mult+1
             i=i+1
             Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Resolver multiplicaciones"
             I.append([i,"Multiplicación"])
        elif isinstance(termino,list) and termino[1]=="/"and Div!=1:
             Div=Div+1
             i=i+1
             Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Resolver divisiones"
             I.append([i,"División"])
        elif isinstance(termino,list) and termino[1]!="/" and termino[1]!="*" and  PARENTESIS!=1:
             PARENTESIS=PARENTESIS+1
             i=i+1
             Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Eliminar paréntesis"
             I.append([i,"Distributiva"])
    if  len(Lista1)==1 and len(Lista2)==1 and isinstance(Lista2[0],tuple):

        if isinstance(Lista1[0],(tuple)):  
            i=i+1
            Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Pasar dividiendo {Estilo.NEGRITA}{formatear_numero(Lista1[0][0])}{Estilo.RESET}"
            I.append([i,"Inverso"])
            
        elif ((Lista1[0][0]==1 and len(Lista1[0])!=3) or isinstance(Lista1[0][0],tuple))  and Lista1[0][len(Lista1[0])-2]=="/":      
            i=i+1
            Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Pasar multiplicando {Estilo.NEGRITA}{formatear_numero(Lista1[0][len(Lista1[0])-1])}{Estilo.RESET}" 
           
            I.append([i,"Inverso"])
        elif not("/"  in Lista1[0])  and not("*"  in Lista1[0]):  
            i=i+1
            Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Pasar dividiendo {Estilo.NEGRITA}{formatear_numero(Lista1[0][0])}{Estilo.RESET}"
            I.append([i,"Inverso"])    
    i=i+1
    Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Pasar términos al otro lado con la operación contraria"
    I.append([i,"Opuesto"])
    i=i+1
    Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Volver a elegir miembro"
    I.append([i,"Miembro"])
    i=i+1
    Texto=Texto+"\n"+f"   {Estilo.CIAN}{i}){Estilo.RESET} Volver a un paso anterior"
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
    Ecuación=input(f"\n{Estilo.AMARILLO}{Estilo.NEGRITA}✎ Ingrese la ecuación que quiera resolver:{Estilo.RESET} \n› ")
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
                 f"""
{Estilo.AZUL}{Estilo.NEGRITA}¿Qué miembro quiere trabajar?{Estilo.RESET}

   {Estilo.CIAN}1){Estilo.RESET} Primer miembro   {Estilo.NEGRITA}{Mostrar_Bonito(Lista1)}{Estilo.RESET}

   {Estilo.CIAN}2){Estilo.RESET} Segundo miembro  {Estilo.NEGRITA}{Mostrar_Bonito(Lista2)}{Estilo.RESET}

   {Estilo.CIAN}3){Estilo.RESET} Cargar otra ecuación
› """)
             if OP1=="1":
                        Texto,I=Lista_Opciones(Lista1,Lista2) 
                        
                        OP2=input(Texto+"\n› " )  
                        Lista_Opciones2(Lista1, Lista2, OP2, I,Manual)
             elif OP1=="2":
                       Texto,I=Lista_Opciones(Lista2, Lista1)
                       OP2=input(Texto+"\n› " )
                       Lista_Opciones2(Lista2, Lista1, OP2, I,Manual)
    
             if OP1!="3"and validarOpcion(OP2,len(I)) and I[int(OP2)-1][1]=="Historial":
                Gestionar_Historial(Lista1, Lista2, Historial,1)
                
        if Condicion_de_corte(Lista1, Lista2)[0]:
            print(caja_ecuacion(Condicion_de_corte(Lista1, Lista2)[1], titulo="Resultado", color=Estilo.VERDE))
        if Condicion_de_corte(Lista2, Lista1)[0]:
            print(caja_ecuacion(Condicion_de_corte(Lista2, Lista1)[1], titulo="Resultado", color=Estilo.VERDE))
            
        input("Presione enter para salir")
    else:
        "Te olvidaste de poner el = y/o escribir el segundo miembro"
def Menu():
    A="1" 
    #1=Modo Manual activado
    Manual=0 
    while A!="5":
        A=input(     
f"""
{Estilo.MAGENTA}{Estilo.NEGRITA}╔══════════════════════════════════╗
║              MENÚ                 ║
╚══════════════════════════════════╝{Estilo.RESET}

                        {Estilo.CIAN}1){Estilo.RESET} Resolver ecuaciones
            
                        {Estilo.CIAN}2){Estilo.RESET} Modo Automático:
    
       En este modo las sumas y resta se resuelven solas, las divisiones y 
       multiplicaciones se pueden resolver haciendo las cuentas  
       o automáticamente, también se pueden saltar la cuentas, en caso de que 
       te trabes. Es el modo por defecto.
       
                           {Estilo.CIAN}3){Estilo.RESET} Modo Manual: 
               
                Las cuentas hay que resolverla manualmente.
                    
              
                        {Estilo.CIAN}4){Estilo.RESET} Cantidad de decimales:
    
       Para comprobar que se hicieron bien la cuentas el programa toma una 
       cierta cantidad de decimales, por defecto redondea en 2 decimales
       por ejemplo 3/4=0,125 en el programa vas a tener que escribir 0,12 
       porque el tecer decimal es menor o igual a 5 si tuvieramos 2/3=0,6666...
       se redondea en 0,67. 
       Para cambiar la cantidad de decimales apreta usa esta opción. 
       Las cuentas se hacen  con una cantidad fija que no cambia lo que cambia
       es la cantidad de decimales que se usan para comprobar un resultado
                       {Estilo.CIAN}5){Estilo.RESET} Salir 
› """)
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
