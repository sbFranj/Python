'''
Diseñe una función llamada palíndromo que tenga como parámetro una cadena de caracteres y devuelva
true si es un palíndromo o false en otro caso. Una palabra es un palíndromo, si se lee igual
misma de izquierda a derecha que de derecha a izquierda, ignorando los blancos,. Por ejemplo: "anilina" o "dabale arroz
a la zorra el abad" Para simplificar el problema, se puede suponer que se utilizan caracteres simples
se utilizan, es decir, sin tildes ni diéresis.

'''



def is_palindrome(string):
    palindrome=True 
    for i in range (len(string)//2):
        if string[i]!=string[(-i-1)]:
            palindrome=False
            
    return palindrome    

print (is_palindrome("azucar"))
print (is_palindrome("dabalearrozalazorraelabad"))



