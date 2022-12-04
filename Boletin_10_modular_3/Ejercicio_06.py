'''
Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.
'''


def buscar_palabra(palabra_buscar, lista):
    encontrada=False
    
    c=0
    c2=0
    while c<(len(lista)):
        if c2<len(palabra_buscar) and palabra_buscar[c2]==lista[c]:
            
            c2+=1
        c+=1
    if c2==len(palabra_buscar):
        encontrada=True    
    return encontrada

print(buscar_palabra("hola", "shybaoxlna"))
print(buscar_palabra("zhola", "shybaoxlna"))
