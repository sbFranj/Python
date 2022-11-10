

tabla=int(input("inserte numero:"))

if 0<tabla<=10:
    for num in range(0, 11):
        print(f"{tabla}*{num}={num*tabla}")
else:
    print("Este numero esta fuera de los limites")