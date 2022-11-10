'''
Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
        a. una lista con todos los que sean primos.
        b. el sumatorio
        c. el promedio de los valores.
        d. una lista con el factorial de cada uno de esos números.
'''
num=1
listanumeros=[]
while num>0:
    num=int(input("Añada numeros a la lista: "))
    listanumeros.append(num)
    
def filtrarNPrimos(lista):
    primos=[]
    for i in range(len(lista)):
        if (lista[i]==2 or lista[i]%2!=0) and (lista[i]==3 or lista[i]%3!=0) and (lista[i]==5 or lista[i]%5!=0) and (lista[i]==7 or lista[i]%7!=0) and (lista[i]==11 or lista[i]%11!=0) and (lista[i]==13 or lista[i]%13!=0)and (lista[i]==17 or lista[i]%17!=0)and (lista[i]==19 or lista[i]%19!=0)and (lista[i]==23 or lista[i]%23!=0)and (lista[i]==29 or lista[i]%29!=0)and (lista[i]==31 or lista[i]%31!=0):
            primos.append(lista[i])
    return primos
def suma(lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
def factorial(numero):    
    total=1  
    for i in range(numero):
        
        total*=i+1
    
    return total
def obtenerFactoriales(lista):
    factoriales=[]
    for i in range(len(lista)):
        factoriales.append(factorial(lista[i]))
    return factoriales


print("a:",filtrarNPrimos(listanumeros))
print("b:",suma(listanumeros)-(listanumeros[-1]))
print("c:",(suma(listanumeros)-(listanumeros[-1]))/len(listanumeros))
print("d:", obtenerFactoriales(listanumeros))







