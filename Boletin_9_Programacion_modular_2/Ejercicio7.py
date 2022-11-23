'''
Diseñe un método llamado isPrime que reciba como parámetro un número entero positivo mayor que 0. 
El método debe devolver True si el número es primo o False si
no es primo. Si el parámetro no es válido el método debe devolver None.
'''


def isPrime(number):
    is_prime=True
    if number>0:
        for i in range(2, number):
            if number%i==0:
                is_prime=False
    else:
        is_prime=None
        
    return f"{number} is prime? {is_prime}"

print(isPrime(-2))
print(isPrime(2))
print(isPrime(652))