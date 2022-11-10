'''
Triángulos. Escribe un programa que pida un número y a continuación pinte un
triángulo como los siguientes utilizando el número como símbolo.
3                4             5
                                  
3                4             5
3 3              4 4           5 5
3 3 3            4 4 4         5 5 5
                 4 4 4 4       5 5 5 5
                               5 5 5 5 5
                               
                secuecia = " "
                for i in range(8)
                    secuencia += str(i)+", "
                print(secuencia)
'''

num=int(input("Introduce numero: "))
secuencia=" "
for i in range(1, num+1):
    secuencia+= str(num*(i**0))
    print(secuencia)