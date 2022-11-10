'''
 Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es impar su familia le regala un puzzle; si es par, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.


        1 año ⇒ recibe 1 puzzle, acumula 1 puzzle|recibe 0€, acumula 0€
        2 años ⇒ recibe 0 puzzle, acumula 1 puzzle|recibe 20€, acumula 20€
        3 años ⇒ recibe 2 puzzle, acumula 3 puzzle|recibe 0€, acumula 20€
        4 años ⇒ recibe 0 puzzle, acumula 3 puzzle|recibe 35€, acumula 55€
        5 años ⇒ recibe 4 puzzle, acumula 7 puzzle|recibe 0€, acumula 55€
        6 años ⇒ recibe 0 puzzle, acumula 7 puzzle|recibe 50€, acumula 105€
        7 años ⇒ recibe 8 puzzle, acumula 15 puzzle|recibe 0€, acumula 105€
        
'''

edad=int(input("Inserte edad: "))
puzzles=1
euros=20
dinero=0

for i in range(1, edad+1):
    
    if i%2==0:
        euros+=15
        dinero+=euros-15       
    elif i%2!=0:
        puzzles*=2
                  
    print(f"{i} años ⇒ {puzzles-1}p y {dinero}€")
   
   
    
        



