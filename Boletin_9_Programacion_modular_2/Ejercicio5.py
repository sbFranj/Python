'''
Diseñe un método llamado powerIt que reciba dos enteros y eleve el primer
número al segundo. Puedes utilizar el producto o la recursión y comprobar los valores. Si
no se proporciona ningún exponente, el primer número se eleva a 0.
'''



def powerIt(base, exponent):
    return base**exponent


base=int(input("Enter an base:"))
exponent=int(input("Enter an exponent:"))

if exponent==None:
    exponent=0
else:
    print(powerIt(base, exponent))