num=10
suma=num
print(f"1º mes: {num}€")
for i in range(2, 21):
    num*=2
    print(f"{i}º mes: {num}€")
    suma+=num
print(suma, "€ en total")
  
    
    