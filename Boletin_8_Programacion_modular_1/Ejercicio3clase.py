'''
Solucion correcta planteada en clase del ejercicio 3
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
