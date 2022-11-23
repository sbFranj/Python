'''
Diseñe un método llamado getPrimeDivisors que reciba un número positivo 
y devuelva una lista con sus divisores primos. Si el parámetro no es válido
el método debe devolver None.
'''

def isPrime(number):
    is_prime=True
    
    for i in range(2, number):
        if number%i==0:
            is_prime=False
   
        
    return is_prime

def getPrimeDivisors(number):
    divisors=[]
    count=0
    count2=1
    if number<0:
        divisors=None
    else:
        if isPrime(number):
            divisors=[1, number]
        else:
            while count<=2:
                if isPrime(count2) and number%count2==0:
                    divisors.append(count2)
                    count+=1
                count2+=1
        
    return divisors

print(getPrimeDivisors(2))
print(getPrimeDivisors(200))
print(getPrimeDivisors(65))