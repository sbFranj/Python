'''
Diseñe un método llamado isFriendNumber que reciba dos números positivos y
devuelva True si los números son amigos, False en caso contrario. Dos números se
consideran amigos si la suma de sus divisores, excepto el número dado, es igual
al segundo y viceversa.
'''

def isFriendNumber(number, number2):
    divisors=0
    is_friend=False
    for i in range(1, number):
        if number%i==0:
            divisors+=i
    
    if divisors==number2:
        is_friend=True 
        
    return is_friend    
    
print(isFriendNumber(220,284))
print(isFriendNumber(1184, 1210))
print(isFriendNumber(300,356))