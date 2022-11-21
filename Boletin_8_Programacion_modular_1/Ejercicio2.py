'''
2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).
'''


listanumeros=[1, 2, 3, 4, 5]

def desplazaNumeros(lista):
    escribe=lista[0]
    guarda=0
    for i in range(len(lista)):
        
        guarda=lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)]=escribe
        escribe=guarda
    return lista

print(desplazaNumeros(listanumeros))
            
            
            
            
        
    
    
    
    
