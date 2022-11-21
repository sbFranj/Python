'''
Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1.
'''




def esBinario(numero):
    binario=True
    if ("1" not in numero) and ("0" not in numero):
        binario=False
    return binario

def riversada(lista):
    listainversa=[]
    for i in range (len(lista)):
        listainversa.append(lista[(i+1)*(-1)])
    return listainversa
    
def conversorBinario_Decimal(numero):
    
    decimal=[]
    sumadecimal=0
    if numero[-1]=="B" and esBinario(numero):
        numero=riversada(numero[0:-1])
        for i in range(len(numero)):
            valor=(2**i)*(int(numero[i]))
            decimal.append(valor)
            sumadecimal+=valor
    
    return sumadecimal

def conversorDecimal_Binario(numero):
    binario=[]
    if numero[-1]=="D":
        numero=numero[0:-1]
        while int(numero)>=2 :
            cociente=int(numero)//2
            resto=int(numero)%2
            binario.append(resto)
            numero=cociente
    binario.append(cociente)
                  
    return binario    

num=0
while num!="-":
    num=input("introduce numero en formato nnnnnnD(para decimal)/nnnnnnB(binario): ").upper()
    
    if esBinario(num):
        mensaje=f"El {num} es {conversorBinario_Decimal(num)}D"
        
    elif num[-1]=="D":
        mensaje=f"El {num} es {riversada(conversorDecimal_Binario(num))}B"
    
    else:
        mensaje="****** Debes de agregar 'D' para decimal o 'B' para binario"
        
    print(mensaje)
           
    
