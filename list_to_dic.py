"""Convierte y lista de tuplas en un diccionario,
donde el primer elemento es la clave y el valor sera
una lista de elementos"""

def list_to_dic(lista):
    """Funcion que pasa una lista a diccionario"""
    dic = {}
    #asigna las claves al diccionario
    for tupla in lista:
        dic[tupla[0]] = []

    #Rellena los valores de las listas
    for clave , valor in dic.items():
        for i in lista:
            if i[0] == clave:
                for j in range(1,len(i)):
                    valor.append(i[j])

    return dic

#programa principal

#lista de ejemplos
l = [('Nolan','Don Pepito'),('Nolan','Don Pedro'),('Buenos','Dias'),
    ('Barcelona','Messi','Puyol','Xavi','Don Andres')]

diccionario = list_to_dic(l) #LLamada a la funcion
print(diccionario) #Imprimiendo diccionario
