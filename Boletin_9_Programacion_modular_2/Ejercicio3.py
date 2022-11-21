'''
Diseñe un método llamado computeDaysInMonth que devuelva el número de días del
el mes y el año que se reciben como argumentos. Puede utilizar el método
leapYear anterior. Si los valores no son válidos el método debe devolver -1.
'''

nameMonth=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def isLeapYear(yyyy):
    return yyyy%4==0 and (yyyy%100!=0 or yyyy%400==0)


def computeDaysInMonth(mm, yyyy):
    maxDaysMonth=31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    if mm==2 and isLeapYear(yyyy):
        maxDaysMonth=29
            
    else:
        maxDaysMonth=maxDaysMonth[mm-1]
        
    return maxDaysMonth

month=1
while month>0:
    month=int(input("Enter a month(mm): "))
    
    year=int(input("Enter a year(yyyy): "))

    if month<=0 or year<=0:
        mensaje=-1
    else:
        mensaje=f"the {nameMonth[month-1]} of {year}, have a {computeDaysInMonth(month,year)} days"
        
    print(mensaje)
    print(" ")


