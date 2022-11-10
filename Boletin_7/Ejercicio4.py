'''
Diseña un programa que reciba el tamaño de una secuencia numérica y muestre en
una única línea cada una de las siguientes secuencias. Si se recibe el número 6 se
imprimiría:
                a. 1, -5, 25, -125, 625, -3125 (-5 elevado)
                b. 1, -1, 0, 1, -1, 0 (modulo 3)
                c. 1, 3, 9, 27, 81, 243  (elevado a i)
                
                secuecia = " "
                for i in range(8)
                    secuencia += str(i)+", "
                print(secuencia)
'''
num=int(input("Introduce un numero: "))

total=" "
for i in range (num):
    total+=str((-5)**i)
    if i< num-1:
        total+=", "
print("a. " +total)

total=" "
for i in range (num):
    total+=str((i%-3)+1)
    if i< num-1:
        total+=", "
print ("b. " + total)

total=" "
for i in range (num):
    total+=str(3**i)
    if i< num-1:
        total+=", "
print ("c. " + total)
