'''
Diseñe un método llamado getNumberOfDigits que reciba un número (puede ser
real, entero, positivo o negativo) y que devuelva el número de dígitos que contiene. Si
el parámetro no es válido, el método debe devolver None. Amplíe esta función a
otros sistemas numéricos (decimal, binario, octal, hexadecimal).

'''
    
def getNumberOfDigitsDecimal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="8" or number[i]=="9" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if(len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]) or ("8"in number[i]) or("9"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsBinary(number):
    count=0     
    listdot=" "
    list0_1=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i] 
        if not(number[i]=="1" or number[i]=="0" or number[i]=="-" or number[i]=="."):
            list0_1+=number[i]   
        if(len(list0_1)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsOctal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if(len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]): 
            count+=1
    
    return count

def getNumberOfDigitsHexadecimal(number):
    count=0     
    listdot=" "
    listothers=""
    for i in range(len(number)):
        if(number[i]=="."):
            listdot+=number[i]
            
        if not(number[i]=="0" or number[i]=="1" or number[i]=="2" or number[i]=="3" or number[i]=="4" or number[i]=="5" or number[i]=="6" or number[i]=="7" or number[i]=="8" or number[i]=="9"or number[i]=="A" or number[i]=="B" or number[i]=="C" or number[i]=="D" or number[i]=="E" or number[i]=="F" or number[i]=="." or number[i]=="-"):
            listothers+=number[i]
        
        if(len(listothers)>0)or("-"in number[1:-1])or("-"in number[-1])or("." in (number[0] or number[-1]))or(".." in number)or(".." in listdot):
            count=None
        elif ("0" in number[i]) or ("1"in number[i]) or ("2"in number[i]) or ("3"in number[i]) or ("4"in number[i]) or ("5"in number[i]) or ("6"in number[i]) or ("7"in number[i]) or ("8"in number[i]) or("9"in number[i])or("A"in number[i])or("B"in number[i])or("C"in number[i])or("D"in number[i])or("E"in number[i])or("F"in number[i]): 
            count+=1
    
    return count
print("[Decimal] tiene", getNumberOfDigitsDecimal("-10.0955"), "digitos")
print("[Binary] tiene", getNumberOfDigitsBinary("1001"), "digitos")
print("[Octal] tiene", getNumberOfDigitsOctal("141"), "digitos")
print("[Hexadecimal] tiene", getNumberOfDigitsHexadecimal("1081A"), "digitos")