'''
3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
   año) y muestre a continuación la fecha en formato largo.
    Introduce el día de la fecha: 15
    Introduce el mes de a fecha: 3
    Introduce el año de a fecha: 2009
    La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.
'''
meses=["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dia=int(input("Introduce dia: "))
while dia>31:
    dia=int(input("EROR; Introduce dia: "))
while dia>0:
        
    mes=int(input("Introduce mes: "))
    while mes<0 or mes>12:
        mes=int(input("EROR; Introduce mes: "))
        
    year=int(input("Introduce year: "))
    while year<0:
        year=int(input("EROR; Introduce year: "))
  
        
    print(f"es {dia} de {meses[mes-1]} de {year}")
    
    dia=int(input("Introduce dia: "))
    while dia>31:
        dia=int(input("EROR; Introduce dia: "))
    
