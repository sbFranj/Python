'''
Diseñe un método llamado getDayOfWeek que reciba una lista con tres enteros
(día, mes y año) y devuelva el día de la semana para esa fecha (lunes
martes, miércoles, jueves, viernes, sábado, domingo).

Puede utilizar el siguiente algoritmo para obtener un número entre 0 (domingo) y 6
(sábado) correspondiente al día de la semana para una fecha determinada:

a = (14 - month) / 12
y = year – a
m = month + 12 * a – 2
d = (day + y + y/4 - y/100 + y/400 + (31*m)/12) mod 7

'''
def getDayOfWeek(day, month, year):
    a=(14-month)/12
    
    y=year-a
    
    m=(month+12)*(a-2)
    
    return(int((day+y)+(y/4)-(y/100)+(y/400)+(31*m)/12)%7)

nameOfDays=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day=1
while day>0:
    day=int(input("Enter a number of day: "))
    month=int(input("Enter a number of month: "))
    year=int(input("Enter a number of year: "))
    if day>0:
        text=nameOfDays[getDayOfWeek(day, month, year)]
        
    else:
        text: "ERROR!"
        
    print("\n",text,"\n")    