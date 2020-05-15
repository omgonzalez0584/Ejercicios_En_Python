"""Escribir una función que reciba una cadena
y devuelva un diccionario con la cantidad
 de apariciones de cada palabra en la cadena
"""

def contar_palabras(cadena):
    lista_cadena = cadena.split(" ")
    dic = {}
    for i in lista_cadena:
        dic[i] = lista_cadena.count(i)
    return dic

cadena = input("Introduzca una cadena: ")
dic_palabras = contar_palabras(cadena)

print(dic_palabras)
