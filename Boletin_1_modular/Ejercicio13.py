'''
Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.
'''

lista_nombres=["Aaron", "Axel", "Dante", "Anya", "Ariadna", "Arida", "Setefilla", "Cara" ]
letra_nombre="A"


def filtroNombres(lista, letra):
    filtrado=[]
    for i in range(len(lista)):
        if lista[i][0]==letra:
            filtrado.append(lista[i])
    return filtrado


print (filtroNombres(lista_nombres, letra_nombre))

#Consultar que datos hay que validar