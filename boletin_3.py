print("Boletin 3")
'''
print("1")
numero = int(input ("inserte numero:"))
if numero%2==0:
    print("es par")
else :
    print("es impar")
print(" ")

print("2")
numero1=int (input("inserte numero:"))
numero2=int (input("inserte numero:"))

if numero1 == numero2:
    print("Los numero son iguales")
    
elif numero1>numero2:
    print("el numero %s es mayor que el numero %s"% (numero1, numero2))

else :   
    print(" el numero %s es mayor que el numero %s"% (numero2, numero1))
print(" ")

print("3")
numero=int(input("inserte numero:"))

if numero%3==0 and numero%2==0:
    print("el numero es multiplo de 2 y multiplo de 3")
elif numero%3==0:
    print("el numero es multiplo de 3")
elif numero%2==0:
    print("el numero es multiplo de 2")
else:
    print(" ")
'''
print("4")

edad=int(input("inserte edad:"))

if edad<100
    if (0<edad<12):
        print("Niño")

    elif 13<edad<17:
        print("Adolescente")
        
    elif 8<edad<29:
        print("Joven")
        
    else :
        print("Adulto")
'''
print("5")
numero1=int(input("inserte 1º numero:"))
numero2=int(input("inserte 2º numero:"))
numero3=int(input("inserte 3º numero:"))
numero4=int(input("inserte 4º numero:"))

media=(numero1+numero2+numero3+numero4)/4
print(("media:"),(numero1+numero2+numero3+numero4)/4)

if numero1>media:
    print(numero1)
    
if numero2>media:
    print(numero2)
    
if numero3>media:
    print(numero3)
    
if numero4>media:
    print(numero4)
    
print("6")
vocal=str(input("inserte letra:"))

if vocal==("a"):
    print("es la primera vocal (A)")
    
if vocal==("e"):
    print("es la segunda vocal (E)")
    
if vocal==("i"):
    print("es la tercera vocal (I)")
    
if vocal==("o"):
    print("es la cuarta vocal (O)")
    
if vocal==("u"):
    print("es la quinta vocal (U)")
    
if vocal!=("a" or "e" or "i" or "o" or "u")  :
    print("no es una vocal")

print("7")

estado_civil=str(input("inserte estado civil:"))
edad=int(input("inserte edad:"))

if (estado_civil==("S")or estado_civil==("D"))and(edad<35):
    print("porcentaje de retencion 12%")
    
if edad>50:
    print("porcentaje de retencion 8,5%")

if (estado_civil==("V")or estado_civil==("C"))and(edad<35):
    print("porcentaje de retencion 11,3%")
    
elif 35<=edad<=50:
    print("porcentaje de retencion 10%")
    


print("8")
hora_1=int(input ("inserte numero de horas(0h a 23h):"))
min_1=int(input ("inserte numero de min(0s a 59s):"))
seg_1=int(input ("inserte numero de segundos(0s a 59s):"))

hora_2=int(input ("inserte 2º numero de horas(0h a 23h):"))
min_2=int(input ("inserte 2º numero de min(0s a 59s):"))
seg_2=int(input ("inserte 2º numero de segundos(0s a 59s):"))

if (0<=hora_1<24) and (0<=hora_2<24) and (0<=min_1<59) and( 0<=min_2<59) and (0<=seg_1<59) and (0<=seg_2<59):
    horario1=(hora_1*3600)+(min_1*60)+seg_1 
    horario2=(hora_2*3600)+(min_2*60)+seg_2 



    if horario1>horario2  :
        print("hora 1" ,hora_1, ":", min_1, ":", seg_1)
        print("hora 2", hora_2 ,":", min_2 ,":" ,seg_2)
        print("hora 1 es mayor")
    
    elif horario1<horario2:
        print("hora 1",hora_1,":",min_1,":",seg_1)
        print("hora 2",hora_2,":",min_2,":",seg_2)
        print("hora 2 es mayor")
    else:
        print("las horas coinciden")
else:
    print("Error")

print("9")

producto=str(input("inserte letra del producto:"))
precio=int(input("inserte precio del producto:"))


if producto == ("A") :
    print((precio*0.93))
    
elif producto==("C") or precio<500:
    print(precio*0.88)

elif producto==("B") or precio<=500:
    print(precio*0.91)
    
else:
    print("Error")

print("10")

numero1=int(input("introducir 1º numero:"))
caracter=str(input("Introducir caracter"))
numero2=int(input("Introducir 2º numero:"))

if caracter ==("+"):
    print (numero1 + numero2)
    
elif caracter==("-"):
    print (numero1 - numero2)

elif caracter==("*"):
    print (numero1 * numero2)
    
elif caracter==("/"):
    print (numero1 // numero2)

else:
    print ("Error")    


'''
        

    