num=int(input("ingrese un numero(negativo para terminar):"))
f=0
while num>0:
    f+=1
    num=int(input("ingrese un numero(negativo para terminar):"))
    if num<0:
        print(f"ha ingresado {f} numeros positivos")

    