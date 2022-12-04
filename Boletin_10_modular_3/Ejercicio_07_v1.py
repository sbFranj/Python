'''
Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la
tercera.
'''
def sustituir_en_frase(frase, sustituida, palabra):
    final=""
    pala=[]
    
    c=0
    c2=0
    c3=0
    while c<(len(frase)):
        pala.append(frase[c])
        c+=1
        if c2<len(sustituida) and frase[c]==sustituida[c2]:
            pala.pop()
            c2+=1
            
            if c2<len(sustituida) and frase[c]!=sustituida[c2] and c3<len(palabra):
                
                pala.append(palabra[c3])
                
                c3+=1
            
    for i in range(len(pala)):
        final+=pala[i]
        
    return final    

print(sustituir_en_frase("la vida es un fastidio maravilloso", "fastidio", "suplicio"))
print(sustituir_en_frase("dale a tu cuerpo alegria macarena", "cuerpo", "body"))



