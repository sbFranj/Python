'''
Diseñe un método llamado computeFactorial que reciba un número entero positivo y
devuelva el factorial de ese número. Si el número es negativo el método debe
retornar Ninguno.
'''

num=int(input("Enter a number: "))

def computeFactorial(number):    
    total=1  
    for i in range(number):
        
        total*=i+1
    
    return total

if num>=0:
    text=computeFactorial(num)
else:
    text="None"    
    
print(text)