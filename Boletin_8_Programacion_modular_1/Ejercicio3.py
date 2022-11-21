'''
3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
   año) y muestre a continuación la fecha en formato largo.
    Introduce el día de la fecha: 15
    Introduce el mes de a fecha: 3
    Introduce el año de a fecha: 2009
    La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
'''
'''
#solucion inicial que plantee(no valida)
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]



dia=1
while dia>0:
    dia=int(input("Introduce dia: "))
    while dia>31:
        dia=int(input("EROR; Introduce dia: "))
        
    mes=int(input("Introduce mes: "))
    while mes<0 or mes>12:
        mes=int(input("EROR; Introduce mes: "))
        
    year=int(input("Introduce year: "))
    while year<0:
        year=int(input("EROR; Introduce year: "))
  
        
    print(f"es {dia} de {meses[mes-1]} de {year}")
'''
def esBisiesto(year):
    return year%4==0 and (year%100!=0 or year%400==0)

def esFechaValida(dd, mm, yyyy):
    diasMaximosPorMes=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    fechaValida= 1<=mm<=12 and ((1<=dd<=diasMaximosPorMes[mm-1]) or (esBisiesto(yyyy) and 1<=dd<=29 and mm==2))
    return fechaValida

def transformarFormatoLargo(dd, mm, yyyy):
    nombreMeses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    if esFechaValida(dd, mm, yyyy):
        mensaje=f"{dd} de {nombreMeses[mm-1]} de {yyyy}"
    
    else:
        mensaje="La fecha no es validad."
    
    return (mensaje)

dia=int(input("Introduce dia: "))
mes=int(input("Introduce mes: "))
anio=int(input("Introduce año: "))
print(transformarFormatoLargo(dia, mes, anio))

while dia>=0:
    dia=int(input("Introduce dia: "))
    mes=int(input("Introduce mes: "))
    anio=int(input("Introduce año: "))
    print(transformarFormatoLargo(dia, mes, anio))

    
